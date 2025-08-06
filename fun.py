import streamlit as st

# Page title
st.title("✨ A Special Message Just for You, Kaushiki 💖")

# Cute header
st.header("_Dear Kaushiki, you are soo :blue[Cute]_ 😎")

# Sweet badges
st.badge("New")
st.badge("Success", icon="✅", color="green")
st.badge("Love", icon="❤️", color="red")

# Career wish message
st.markdown("""
### 🌸 **Wishing You All the Success in Your Career**
> _May your dreams be bigger than your fears and your actions louder than your words._
>
> You are smart, talented, and full of potential – I believe in you and I know you're going to achieve amazing things! 🚀🌟  
> I’ll be cheering for you always.

""")

# Heart using LaTeX
st.latex(r"\Huge \textcolor{red}{\heartsuit}")

# Closing message
st.markdown("""
---
### 💌 Always with you,  
**_Your biggest fan ✨_**
""")
