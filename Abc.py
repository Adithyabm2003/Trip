import streamlit as st
from gradio_client import Client

# Initialize the Gradio client
client = Client("m-ric/ai-travel-planner")

# Title of the app
st.title("AI Trip Planner")

# Input fields for user input
travel_days = st.text_input("Travel Days:")
destination = st.text_input("Destination:")
travel_style = st.text_input("Travel Style:")

# When the user clicks the button, generate the trip plan
if st.button("Plan Trip"):
    # Generate the trip description
    trip_description = f"A {travel_days}-day {travel_style} trip to {destination}."

    try:
        # Call the Gradio API
        result = client.predict(
            text=trip_description,
            api_name="/run_display"
        )

        # Extract data from the result
        chosen_locations = result[0]  # Dictionary containing locations
        trip_summary = result[1]      # Summary string
        print(chosen_locations)
        
        # Display the trip summary
        st.subheader("Trip Summary:")
        st.write(trip_summary)

        # Display each chosen location
        # st.subheader("Chosen Locations:")
        # for location in chosen_locations:
        #     st.markdown(f"### {location['name']}")
        #     st.write(location['description'])

    except Exception as e:
        st.error(f"An error occurred: {e}")
