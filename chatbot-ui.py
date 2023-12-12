import streamlit as st



# A simple Hello World Message
#with st.chat_message("user"):
#	st.write("Hello World")


#prompt = st.chat_input("Say something.")
#if prompt:
#	st.write("Whatever you say now, I will just repeat it again.")
#	st.write(f"{prompt}")
#	st.write("Scroll here is disabled.")

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
	st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
	st.chat_message("user").markdown(prompt)
    # Add user message to chat history
	st.session_state.messages.append({"role": "user", "content": prompt})

	response = f"Echo: {prompt}"
    # Display assistant response in chat message container

	with st.chat_message("assistant"):
		st.markdown(response)
    # Add assistant response to chat history
	st.session_state.messages.append({"role": "assistant", "content": response})
