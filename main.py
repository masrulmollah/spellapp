import streamlit as st

# Initialize session state for score
if 'score' not in st.session_state:
    st.session_state.score = 0

# List of images and corresponding correct spellings
images = {
    "Apple": "apple.jpg",
    "Mango": "mango.jpg",
    "Banana": "banana.jpg",
    "Cat": "cat.jpg",
    "Tree": "tree.jpg"
}

# Create a list of serial numbers for the dropdown
image_keys = list(images.keys())
serial_numbers = [f"Image {i+1}" for i in range(len(image_keys))]

# Function to check spelling
def check_spelling(correct_spelling, user_input):
    if user_input.lower() == correct_spelling.lower():
        st.session_state.score += 10
        return "Right!"
    else:
        st.session_state.score -= 10
        return "Wrong!"

# Center the content and add background color
st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        color: #4CAF50; /* Green color for score */
        background-color: #f0f0f0; /* Light grey background for score */
        padding: 10px;
        border-radius: 10px;
    }
    .centered-title {
        text-align: center;
        color: #2196F3; /* Blue color for title */
        background-color: #e0f7fa; /* Light blue background for title */
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
    }
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the score at the top with color, background, and centered
st.markdown(f"<h1 class='centered-text'>Current Score: {st.session_state.score}</h1>", unsafe_allow_html=True)

# Title with color, background, and centered
#st.markdown("<h2 class='centered-title'>Spelling Game</h2>", unsafe_allow_html=True)

# Dropdown to select the image by serial number
selected_serial = st.selectbox("Choose an image:", serial_numbers)
selected_image_key = image_keys[serial_numbers.index(selected_serial)]

# Display the selected image
st.image(images[selected_image_key], caption=f"What is this?", use_column_width=False, width=300)

# Correct spelling of the word
correct_spelling = selected_image_key  # The correct word is the key of the selected image

# User input and check button in the same row
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("Spell the word:")
with col2:
    if st.button("Check"):
        if user_input:
            result = check_spelling(correct_spelling, user_input)
            st.markdown(f"<h1 class='centered-text'>{result}</h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 class='centered-text'>Please enter a spelling!</h1>", unsafe_allow_html=True)

# Centering the reset button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Reset Score"):
        st.session_state.score = 0
        st.write("Score has been reset.")
        st.markdown(f"<h1 class='centered-text'>Current Score: {st.session_state.score}</h1>", unsafe_allow_html=True)
