import streamlit as st
import pandas as pd
from src.contact_book import db, utils, validators

db.init_db()

st.set_page_config(page_title="Contact Book", layout="wide")
st.title("📖 Contact Book")

# Sidebar - Add new contact
st.sidebar.header("➕ Add Contact")
with st.sidebar.form("contact_form"):
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    address = st.text_area("Address")
    submitted = st.form_submit_button("Add")
    if submitted and name:
        if phone and not validators.is_valid_phone(phone):
            st.sidebar.error("Invalid phone number (7–15 digits required)")
        elif email and not validators.is_valid_email(email):
            st.sidebar.error("Invalid email address")
        else:
            utils.add_contact(name, phone, email, address)
            st.sidebar.success("Contact added!")

# Main area - List contacts
st.subheader("📋 All Contacts")
contacts = utils.get_contacts()
if contacts:
    df = pd.DataFrame(contacts, columns=["ID", "Name", "Phone", "Email", "Address"])
    st.dataframe(df.set_index("ID"), use_container_width=True)

    # Select contact for update/delete
    ids = df["ID"].tolist()
    selected_id = st.selectbox("Select Contact ID", ids)

    col1, col2 = st.columns(2)
    with col1:
        st.write("✏ Update Contact")
        new_name = st.text_input("Update Name", value=df.loc[df["ID"] == selected_id, "Name"].values[0])
        new_phone = st.text_input("Update Phone", value=df.loc[df["ID"] == selected_id, "Phone"].values[0])
        new_email = st.text_input("Update Email", value=df.loc[df["ID"] == selected_id, "Email"].values[0])
        new_address = st.text_area("Update Address", value=df.loc[df["ID"] == selected_id, "Address"].values[0])
        if st.button("Update"):
            if new_phone and not validators.is_valid_phone(new_phone):
                st.error("Invalid phone number")
            elif new_email and not validators.is_valid_email(new_email):
                st.error("Invalid email")
            else:
                utils.update_contact(selected_id, new_name, new_phone, new_email, new_address)
                st.success(f"Contact {selected_id} updated!")

    with col2:
        st.write("🗑 Delete Contact")
        if st.button("Delete"):
            utils.delete_contact(selected_id)
            st.warning(f"Contact {selected_id} deleted!")

    # Export to CSV
    st.download_button("⬇ Export Contacts to CSV",
                       data=df.to_csv(index=False),
                       file_name="contacts.csv",
                       mime="text/csv")
else:
    st.info("No contacts found. Add one from the sidebar!")
