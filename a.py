import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("💖 yêu em Trang💖")

# Hàm vẽ hình trái tim
def draw_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=3)
    ax.fill(x, y, 'red', alpha=0.6)
    ax.set_aspect("equal")
    ax.axis("off")

    return fig

# Hiển thị hình trái tim
st.pyplot(draw_heart())
