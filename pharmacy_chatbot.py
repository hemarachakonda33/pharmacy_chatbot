#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Install dependencies:
# pip install streamlit google-genai

import os
import streamlit as st
from google import genai
from google.genai import types

# Page config
st.set_page_config(
    page_title="Pharmacy Prescription Handling Explainer",
    page_icon="💊",
    layout="centered"
)

st.title("💊 Pharmacy Prescription Handling & Storage Explainer Bot")
st.caption("Educational use only • No medical advice")

# Input box
user_input = st.text_area(
    "Ask a question about pharmacy operations:",
    placeholder="Example: Explain prescription handling rules"
)

# Gemini client
def get_response(prompt):
    client = genai.Client(
        api_key=("AIzaSyB7KBVIkcSrMo-J7MHh2pliTsVOFhDCubs")
    )

    model = "gemini-3-flash-preview"

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH"
        )
    )

    response_text = ""

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config
    ):
        if chunk.text:
            response_text += chunk.text

    return response_text


# Button action
if st.button("Explain"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating explanation..."):
            response = get_response(user_input)
            st.markdown("### Explanation")
            st.write(response)

# Footer
st.markdown("---")
st.caption(
    "This bot explains pharmacy procedures and safety guidelines only. "
    "It does not provide medical advice or medication recommendations."
)

