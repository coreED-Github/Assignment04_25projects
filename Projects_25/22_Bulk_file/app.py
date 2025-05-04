import streamlit as st
import os
import shutil
from pathlib import Path

st.title("📁 Bulk File Renamer App")
st.markdown("Upload multiple files or a folder, and rename all files in bulk based on your rules.")

uploaded_files = st.file_uploader(
    "Upload your files (drag and drop supported)", 
    accept_multiple_files=True, 
    type=None
)

upload_dir = Path("uploaded_files")
upload_dir.mkdir(exist_ok=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        with open(upload_dir / uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success(f"{len(uploaded_files)} files uploaded successfully!")

    st.write("### Uploaded Files:")
    for file in uploaded_files:
        st.write(file.name)

    st.write("---")

    st.write("## 📝 Rename Options")

    prefix = st.text_input("Add Prefix (Optional)", "")
    suffix = st.text_input("Add Suffix (Optional)", "")
    start_number = st.number_input("Start Numbering from", min_value=1, step=1, value=1)
    numbering = st.checkbox("Add numbering to filenames")

    if st.button("🔁 Rename Files"):
        renamed_files = []
        files = list(upload_dir.iterdir())
        for i, file_path in enumerate(files, start=start_number):
            ext = file_path.suffix
            original_name = file_path.stem
            new_name = ""

            if numbering:
                new_name = f"{prefix}{i}{suffix}{ext}"
            else:
                new_name = f"{prefix}{original_name}{suffix}{ext}"

            new_path = file_path.parent / new_name
            os.rename(file_path, new_path)
            renamed_files.append(new_name)

        st.success("Files renamed successfully!")
        st.write("### Renamed Files:")
        for name in renamed_files:
            st.write(name)

        shutil.make_archive("renamed_files", 'zip', upload_dir)
        with open("renamed_files.zip", "rb") as f:
            st.download_button(
                label="⬇️ Download Renamed Files as ZIP",
                data=f,
                file_name="renamed_files.zip",
                mime="application/zip"
            )
