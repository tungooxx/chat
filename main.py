import streamlit as st
from streamlit_chat import message

# Tạo một hàm để xử lý đầu vào từ người dùng và tạo ra các phản hồi
st.title("Chatbot")

# Lưu trữ đầu vào
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Tạo một hàm để trả về đầu vào của người dùng từ một trường nhập văn bản
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

# Hàm để tạo ra các phản hồi dựa trên đầu vào của người dùng
def generate_response(user_input):
    if "hello" in user_input.lower():
        return "Hello, I am the chatbot."
    elif "how are you" in user_input.lower():
        return "Today is a great day!"
    else:
        return "I'm not sure how to respond to that."

# Tạo ra phản hồi bằng cách sử dụng hàm 'generate_response' và lưu nó vào biến 'output'
user_input = get_text()

if user_input:
    output = generate_response(user_input)

    # Lưu trữ đầu vào và đầu ra
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# Hiển thị lịch sử trò chuyện
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
