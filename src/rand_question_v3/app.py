import random
import time

import streamlit as st

from rand_question_v3.data import name_list, questions
from rand_question_v3.selector import random_choice

st.title("Random Student & Question Picker")

if "remaining_names" not in st.session_state:
    st.session_state.remaining_names = name_list.copy()

st.write(f"Students remaining: {len(st.session_state.remaining_names)}")
st.write(", ".join(st.session_state.remaining_names))

placeholder = st.empty()

if len(st.session_state.remaining_names) == 0:
    st.write("All names have been chosen.")
elif st.button("Pick a student"):
    # Flash random combos while slowing down, then land on the real pick.
    spin_steps = 15
    for step in range(spin_steps):
        flash_name = random.choice(st.session_state.remaining_names)
        flash_question = random.choice(questions)
        placeholder.markdown(f"### {flash_name} — {flash_question}")
        time.sleep(0.05 + step * 0.02)

    result = random_choice(st.session_state.remaining_names, questions)
    placeholder.markdown(f"### {result}")

    chosen_name = result.split("**")[1]
    st.session_state.remaining_names.remove(chosen_name)

if st.button("Reset"):
    st.session_state.remaining_names = name_list.copy()
    st.rerun()
