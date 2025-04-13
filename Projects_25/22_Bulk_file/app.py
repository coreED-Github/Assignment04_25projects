import os
import streamlit as st
import datetime

def rename_files(folder_path, prefix, suffix, case, find_word, replace_word):
    try:
        files = os.listdir(folder_path)
        renamed_files = []
        for file in files:
            old_name = os.path.join(folder_path, file)
            new_name = file

            if prefix:
                new_name = prefix + new_name
            if suffix:
                new_name = new_name + suffix

            if case == "Uppercase":
                new_name = new_name.upper()
            elif case == "Lowercase":
                new_name = new_name.lower()

            if find_word and replace_word:
                new_name = new_name.replace(find_word, replace_word)

            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            new_name = f"{new_name}_{current_date}"

            new_name_path = os.path.join(folder_path, new_name)
            os.rename(old_name, new_name_path)
            renamed_files.append((old_name, new_name_path))

        return renamed_files
    except Exception as e:
        st.error(f"Error: {e}")
        return []

st.title("Bulk File Renamer")
st.write("Rename your files based on specific conditions.")

folder_path = st.text_input("Enter the folder path:")

prefix = st.text_input("Prefix to add:")
suffix = st.text_input("Suffix to add:")
case = st.selectbox("Change case:", ["None", "Uppercase", "Lowercase"])
find_word = st.text_input("Find word to replace:")
replace_word = st.text_input("Replace with:")

if st.button("Rename Files"):
    if folder_path:
        renamed_files = rename_files(folder_path, prefix, suffix, case, find_word, replace_word)
        if renamed_files:
            st.success("Files renamed successfully!")
            st.write("Renamed Files:")
            for old_name, new_name in renamed_files:
                st.write(f"{old_name} -> {new_name}")
        else:
            st.error("No files renamed.")
    else:
        st.warning("Please enter a valid folder path.")