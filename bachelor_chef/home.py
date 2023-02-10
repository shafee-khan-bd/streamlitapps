import openai
import streamlit as st
from functools import lru_cache
import plotly.express as px
from skimage import io
import webbrowser

## Set up OpenAI API client
#openai.api_key = st.secrets.api_key
## Use OpenAI's GPT-3 to generate names based on selected language and keywords
#@lru_cache(maxsize=128)
#def generate_recipe_with_prompt(food_style, spices, proteins, veggies, addon):
#    """
#    Use OpenAI's GPT-3 to generate a recipe based on the selected food style, spices, proteins, and vegetables
#    """
#    model_engine = "text-davinci-003"
#    prompt = (
#        f"Generate a simple and easy to cook {food_style} cuisine recipe. Kitchen inventory includes "
#        f"following spices {spices}, proteins {proteins}, veggies {veggies} and additional items {addon}. Use metric system for quantity. "
#        f"Also provide a prompt for DALL-E 2 to create a visualization for this recipe."
#    )
#
#    completions = openai.Completion.create(
#        engine=model_engine,
#        prompt=prompt,
#        max_tokens=1024,
#        n=1,
#        stop=None,
#        temperature=0.5,
#    )
#
#    message = completions.choices[0].text
#    return message.strip().split("\n\n")
#
#### create image from prompt 
#def generate_image_for_recipe(prompt):
#    
#    response = openai.Image.create(
#      prompt= prompt,
#      n=1,
#      size="1024x1024"
#    )
#    image_url = response['data'][0]['url']
#    return image_url
#
#
## list of food styles
#food_styles = ["Bangladeshi", "Indian", "Chinese", "Italian", "French"]
#
#
## list of spices
#spices = [
#    "Cumin (Jeera)",
#    "Coriander (Dhania)",
#    "Turmeric (Haldi)",
#    "Red Chili Powder (Lal Mirch Powder)",
#    "Ginger Powder (Adrak Powder)",
#    "Garlic Powder (Lasun Powder)",
#    "Cinnamon (Dalchini)",
#    "Cloves (Laung)",
#    "Cardamom (Elaichi)",
#    "Mustard Seeds (Sarason)",
#    "Fenugreek (Methi)",
#    "Bay Leaves (Tej Patta)",
#    "Black Pepper (Kali Mirch)",
#    "Mace (Javitri)",
#    "Star Anise (Chakra Phool)",
#    "Coriander Seeds (Dhania Dana)",
#    "Cumin Seeds (Jeera Dana)",
#    "Nigella Seeds (Kalonji)",
#    "Caraway Seeds (Shahi Jeera)",
#    "Fennel Seeds (Saunf)",
#    "Curry Leaves (Kadi Patta)",
#    "Celery Seeds (Ajmoda)",
#    "Mustard Powder (Sarason Powder)",
#    "Cayenne Pepper (Lal Mirch)",
#    "Nutmeg (Jaiphal)",
#    "Allspice (Sabut Karafs)",
#    "Sesame Seeds (Til)",
#    "Black Cumin Seeds (Shahi Jeera)",
#    "Aniseed (Sauf)",
#    "Mint Leaves (Pudina Patta)",
#]
#
#
## list of proteins
#proteins = ["Chicken (Murgi)", "Beef (Gosht)", "Egg (Dim)",
#            "Lamb (Bakr)", "Small Fish (Mach)", 
#            "Big Fish (Mach)", "Prawn (Chingri)"]
#
## list of veggies
#veggies = [
#    "Tomato (Tamatar)",
#    "Potato (Aalu)",
#    "Eggplant (Begun)",
#    "Okra (Bhindi)",
#    "Bitter Gourd (Karela)",
#    "Pumpkin (Kaddu)",
#    "Beans (Moong Dal)",
#    "Carrot (Gajar)",
#    "Cauliflower (Phool Gobhi)",
#    "Onion (Pyaaz)",
#    "Radish (Muli)",
#    "Green Chilli (Hari Mirch)",
#    "Green Peas (Matar)",
#    "Garlic (Lehsun)",
#    "Ginger (Adrak)",
#    "Lemon (Nimbu)",
#    "Sweet Potato (Shakarkandi)",
#    "Ladyfinger (Bhindi)",
#    "Cucumber (Kheera)",
#    "Colocassia (Arbi)",
#    "Spinach (Palak)",
#    "Bottle Gourd (Lauki)",
#    "Turnip (Shalgam)",
#    "Brinjal (Baingan)",
#    "Mustard Greens (Sarsoon ka Saag)",
#    "Mushroom (Khumb)",
#    "Red Chilli (Lal Mirch)",
#    "Ridge Gourd (Turai)",
#    "Zucchini (Tori)"
#]
#
## Main page layout
#st.sidebar.title("Food Recipe Generator")
#
## Food style selectbox
#selected_food_style = st.sidebar.selectbox("Select food style", food_styles, index=0)
#
## Spice list multiselect
#selected_spices = st.sidebar.multiselect("Select spices", spices, default=spices[:5])
#
## Protein list multiselect
#selected_proteins = st.sidebar.multiselect("Select protein", proteins, default=None)
#
## Vegetable list multiselect
#selected_veggies = st.sidebar.multiselect("Select veggies", veggies, default=veggies[:3])
#
## Additional items list
#selected_addons = st.sidebar.text_input("Write additional items separated by comma (,)")
#
## Buttons on top
#col1, col2 = st.columns(2)
#with col1:
#    generate_recipe = st.button("Click to see Bachelor-Chef's magic")
#with col2:
#    if st.button('Youtube Channel'):
#        webbrowser.open_new_tab('https://youtube.com/@shafeekhan-1step')
#
#
## Button to trigger the recipe generation
#if generate_recipe:
#    # Progress bar to show the status of the recipe generation
#    mybar = st.progress(0.1)
#    
#    # Generate the recipe using the selected inputs
#    response = generate_recipe_with_prompt(selected_food_style, tuple(selected_spices), tuple(selected_proteins), tuple(selected_veggies), selected_addons)
#    recipe_title = response[0]
#    ingredients = response[1]
#    instructions = response[2]
#    dalle_prompt = str(response[3])
#    
#    # Show the recipe title
#    st.subheader(recipe_title)
#    
#    # Update the progress bar
#    mybar.progress(0.4)
#    
#    # Use a container to show the ingredients and instructions in two columns
#    with st.container():
#        col1, col2 = st.columns([2,1])
#        with col1:
#            st.write(ingredients)
#        with col2:
#            st.write(instructions)
#            
#            # Update the progress bar
#            mybar.progress(0.8)
#
#    # Use another container to show the generated image for the recipe
#    with st.container():
#        # Extract the DALL-E prompt from the response
#        prompt = dalle_prompt.replace('Prompt for DALL-E 2:','')
#        
#        # Generate the image for the recipe using the DALL-E prompt
#        image_url = generate_image_for_recipe(prompt)
#        img = io.imread(image_url)
#        
#        # Add a separator line
#        st.write("##")
#        
#        # Update the progress bar
#        mybar.progress(0.9)
#        
#        # Show the DALL-E prompt
#        st.write(prompt)
#        
#        # Plot the image for the recipe
#        fig  = px.imshow(img, binary_format = 'png')
#        fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
#        st.plotly_chart(fig, use_container_width=True)
#        
#        # Update the progress bar to 100%
#        mybar.progress(1.0)
#        st.balloons()
#

