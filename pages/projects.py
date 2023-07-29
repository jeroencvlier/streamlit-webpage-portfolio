from pages.utils import *

load_css()
# st.markdown(
#     """
#     <style>
#     .myButton {
#         display: inline-block;
#         position: relative;
#         padding: 10px 20px;
#         border: 4px solid transparent;  /* Initial border, transparent */
#         border-radius: 15px;  /* Adjust as needed */
#         font-size: 1em;
#         text-decoration: none; /* Removes underline */
#         height: 110px;
#         width: 100%;  /* Set width to 100% */
#         overflow: hidden;
#         z-index: 1;
#     }

#     .myButton:hover {
#         border: 4px solid;  /* Border on hover */
#         background-color: rgb(211,211,211);
#         transition: background-color 5.0s ease;
#     }

#     .myButton:hover::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         right: 0;
#         bottom: 0;
#         left: 0;
#         border: 4px solid;
#         border-image: linear-gradient(270deg, red, blue);
#         border-image-slice: 1;
#         border-radius: 15px; /* Same radius as the button */
#         z-index: -1;
#         animation: Gradient 6s ease infinite;
#     }

#     @keyframes Gradient {
#         0% {
#             border-image-source: linear-gradient(270deg, red, blue, red);
#         }
#         50% {
#             border-image-source: linear-gradient(270deg, blue, red, blue);
#         }
#         100% {
#             border-image-source: linear-gradient(270deg, red, blue, red);
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # ...rest of your code


# projects13 = ["project1", "project2", "project3"]
# projects46 = ["project4", "project5", "project6"]
# projects79 = ["project7","project8"]

# for project in [projects13, projects46, projects79]:
#     if len(project) == 1:
#         _,col,_ = st.columns([0.33,0.33,0.33])
#         columns = [col]
#     if len(project) == 2:
#         _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
#         columns = [left,right]
#     if len(project) == 3:
#         columns = st.columns(3)
        
#     for col, proj in zip(columns, project):                
#         with col:
#             st.markdown(f"<button class='myButton'>{proj}</button>", unsafe_allow_html=True)

# st.markdown(
#     """
#     <style>
#     .myButton {
#         display: inline-block;
#         position: relative;
#         padding: 10px 20px;
#         border: 4px solid transparent;
#         border-radius: 15px;
#         font-size: 1em;
#         text-decoration: none;
#         height: 110px;
#         width: 100%;
#         overflow: hidden;
#         z-index: 1;
#     }

#     .myButton::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         right: 0;
#         bottom: 0;
#         left: 0;
#         border: 4px solid;
#         border-image: linear-gradient(270deg, red, blue, red);
#         border-image-slice: 1;
#         z-index: -1;
#         border-radius: inherit;
#         background-color: rgb(211,211,211);
#     }

#     .myButton:hover::before {
#         animation: Gradient 3s ease infinite;
#     }

#     .myButton:hover {
#         background-color: rgb(211,211,211);
#     }

#     @keyframes Gradient {
#         0% {
#             border-image-source: linear-gradient(270deg, red, blue, red);
#         }
#         50% {
#             border-image-source: linear-gradient(270deg, blue, red, blue);
#         }
#         100% {
#             border-image-source: linear-gradient(270deg, red, blue, red);
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # ...rest of your code

# projects13 = ["project1", "project2", "project3"]
# projects46 = ["project4", "project5", "project6"]
# projects79 = ["project7","project8"]

# for project in [projects13, projects46, projects79]:
#     if len(project) == 1:
#         _,col,_ = st.columns([0.33,0.33,0.33])
#         columns = [col]
#     if len(project) == 2:
#         _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
#         columns = [left,right]
#     if len(project) == 3:
#         columns = st.columns(3)
        
#     for col, proj in zip(columns, project):                
#         with col:
#             st.markdown(f"<button class='myButton'>{proj}</button>", unsafe_allow_html=True)


# st.markdown(
#     """
#     <style>
#     h1 {
#         font-size: 2.5em;
#         background: -webkit-linear-gradient(to bottom right, red, blue);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: pink;
#         text-align: center;
#     }
#     </style>
#     <h1>Project Page</h1>
#     """,
#     unsafe_allow_html=True,
# )


# st.markdown("<h1 style='text-align: center; color: white;'>Project Page</h1>", unsafe_allow_html=True)
# st.markdown(
#     """
#     <style>
#     .myButton {
#         display: inline-block;
#         position: relative;
#         padding: 10px 20px;
#         border: 4px solid transparent;
#         border-radius: 15px;
#         font-size: 1em;
#         text-decoration: none;
#         height: 110px;
#         width: 100%;
#         overflow: hidden;
#         z-index: 1;
#     }

#     .myButton::before {
#         content: '';
#         position: absolute;
#         top: -4px;
#         right: -4px;
#         bottom: -4px;
#         left: -4px;
#         z-index: -1;
#         background: linear-gradient(270deg, red, blue);
#         background-size: 200% 200%;
#         border-radius: inherit;  
#         animation: Gradient 3s ease infinite;
#     }

#     .myButton:hover {
#         background-color: rgb(211,211,211);
#         transition: background-color 0.5s ease;
#     }

#     @keyframes Gradient {
#         0% {
#             background-position: 0% 50%;
#         }
#         50% {
#             background-position: 100% 50%;
#         }
#         100% {
#             background-position: 0% 50%;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)

# ...rest of your code

# --------------------------------------------------------------
# 
# --------------------------------------------------------------

# st.markdown(
#     """
# <style>
# button {
#     height: 110px;  
# }
# div.PortMarker {
#     box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
#     border-radius: 15px;
#     padding: 5% 5% 5% 10%;
# }
# </style>
# """,
#     unsafe_allow_html=True,
# )



# projects13 = ["project1", "project2", "project3"]
# projects46 = ["project4", "project5", "project6"]
# projects79 = ["project7","project8"]


# for project in [projects13, projects46, projects79]:
#     if len(project) == 1:
#         _,col,_ = st.columns([0.33,0.33,0.33])
#         columns = [col]
#     if len(project) == 2:
#        _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
#        columns = [left,right]
#     if len(project) == 3:
#         columns = st.columns(3)
        
#     for col, proj in zip(columns, project):                
#         with col:


#             if st.button(proj, use_container_width=True):
#                 pass
            
            
# --------------------------------------------------------------
# 
# --------------------------------------------------------------
# st.markdown(
#     """
# <style>
#     .myButton {
#         display: inline-block;
#         position: relative;
#         padding: 10px 20px;
#         border: 4px solid transparent;  /* Initial border, transparent */
#         border-radius: 15px;  /* Adjust as needed */
#         font-size: 1em;
#         text-decoration: none; /* Removes underline */
#         height: 110px;
#         width: 100%;  /* Set width to 100% */
#     }

#     .myButton:hover {
#         border: 4px solid;  /* Border on hover */
#         border-image: linear-gradient(to bottom right, red, blue) 1; /* Apply the gradient as border image on hover. */
#         border-radius: 15px;  /* Adjust as needed */
#         background-color: rgb(211,211,211);
#         transition: background-color 0.5s ease;
#     }
# </style>
# """, unsafe_allow_html=True)

# ...rest of your code


# --------------------------------------------------------------
# 
# --------------------------------------------------------------
# st.markdown(
#     """
# <style>
#     .gradient-border {
#         display: inline-block;
#         position: relative;
#         padding: 5px;
#         border: 4px solid;  /* Specify the border width here. */
#         border-image: linear-gradient(to right, red, blue) 1; /* Apply the gradient as border image. */
#         border-radius: 5px;
#     }

#     .gradient-border a {
#         position: relative;
#         z-index: 1;
#         border: none;
#         background: transparent;
#         padding: 10px 20px;
#         font-size: 1em;
#         border-radius: 5px;
#         color: inherit; /* Or any color you want */
#         text-decoration: none; /* Removes underline */
#     }
# </style>
# """, unsafe_allow_html=True)


# projects13 = ["project1", "project2", "project3"]
# projects46 = ["project4", "project5", "project6"]
# projects79 = ["project7","project8"]

# for project in [projects13, projects46, projects79]:
#     if len(project) == 1:
#         _,col,_ = st.columns([0.33,0.33,0.33])
#         columns = [col]
#     if len(project) == 2:
#        _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
#        columns = [left,right]
#     if len(project) == 3:
#         columns = st.columns(3)
        
#     for col, proj in zip(columns, project):                
#         with col:
#             st.markdown(
#                     f"""
#                 <div class="gradient-border">
#                     <a href="#">{proj}</a>
#                 </div>
#                 """,
#                     unsafe_allow_html=True,
#                 )
# projects13 = ["project1", "project2", "project3"]
# projects46 = ["project4", "project5", "project6"]
# projects79 = ["project7","project8"]

# for project in [projects13, projects46, projects79]:
#     if len(project) == 1:
#         _,col,_ = st.columns([0.33,0.33,0.33])
#         columns = [col]
#     if len(project) == 2:
#         _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
#         columns = [left,right]
#     if len(project) == 3:
#         columns = st.columns(3)

#     for col, proj in zip(columns, project):                
#         with col:
#             if st.button(proj,use_container_width=True):
#                 # handle click here
#                 pass
# st.markdown(
#     """
#     <style>
#     .myButton {
#         display: inline-block;
#         position: relative;
#         padding: 10px 20px;
#         border: 4px solid transparent;
#         border-radius: 15px;
#         font-size: 1em;
#         text-decoration: none;
#         height: 110px;
#         width: 100%;
#         overflow: hidden;
#         z-index: 1;
#     }

#     .myButton::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         right: 0;
#         bottom: 0;
#         left: 0;
#         border: 4px solid;
#         border-image: linear-gradient(270deg, red, blue, red);
#         border-image-slice: 1;
#         z-index: -1;
#         border-radius: inherit;
#         animation: Gradient 3s ease infinite;
#         background-color: rgb(211,211,211);
#     }

#     .myButton:hover {
#         background-color: rgb(211,211,211);
#     }

#     @keyframes Gradient {
#         0% {
#             border-image-source: linear-gradient(270deg, red, blue, red);
#         }
#         50% {
#             border-image-source: linear-gradient(270deg, blue, red, blue);
#         }
#         100% {
#             border-image-source: linear-gradient(270deg, red, blue, red);
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # ...rest of your code


# projects13 = ["project1", "project2", "project3"]
# projects46 = ["project4", "project5", "project6"]
# projects79 = ["project7","project8"]

# for project in [projects13, projects46,projects79]:
#     if len(project) == 1:
#         _,col,_ = st.columns([0.33,0.33,0.33])
#         columns = [col]
#     if len(project) == 2:
#         _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
#         columns = [left,right]
#     if len(project) == 3:
#         columns = st.columns(3)
        
#     for col, proj in zip(columns, project):                
#         with col:
#             st.markdown(f"<button class='myButton'>{proj}</button>", unsafe_allow_html=True)
# st.markdown(
#     """
#     <style>
#     .myButton {
#         display: inline-block;
#         position: relative;
#         padding: 10px 20px;
#         border: 4px solid;  /* Initial border */
#         border-image: linear-gradient(to bottom right, red, blue) 1; /* Apply the gradient as border image. */
#         border-radius: 15px;  /* Adjust as needed */
#         font-size: 1em;
#         text-decoration: none; /* Removes underline */
#         height: 110px;
#         width: 100%;  /* Set width to 100% */
#         background-color: rgb(211,211,211);
#     }

#     .myButton:hover {
#         background-color: rgb(169,169,169);  /* Darker background color on hover */
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # ...rest of your code


# projects13 = ["project1", "project2", "project3"]
# projects46 = ["project4", "project5", "project6"]
# projects79 = ["project7","project8"]

# for project in [projects13, projects46,projects79]:
#     if len(project) == 1:
#         _,col,_ = st.columns([0.33,0.33,0.33])
#         columns = [col]
#     if len(project) == 2:
#         _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
#         columns = [left,right]
#     if len(project) == 3:
#         columns = st.columns(3)
        
#     for col, proj in zip(columns, project):                
#         with col:
#             st.markdown(f"<button class='myButton'>{proj}</button>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .myButton {
        border-radius: 20px;
        display: inline-block;
        position: relative;
        padding: 10px 20px;
        border: 4px solid;  /* Initial border */
        border-image: linear-gradient(to bottom right, red, blue) 1;
        font-size: 1em;
        text-decoration: none; /* Removes underline */
        height: 110px;
        width: 100%;  /* Set width to 100% */
        background-color: rgb(211,211,211);
        overflow: hidden; /* Ensure the content doesn't overflow the border */
    }

    .myButton:hover {
        background-color: rgb(169,169,169);  /* Darker background color on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# ...rest of your code

projects13 = ["project1", "project2", "project3"]
projects46 = ["project4", "project5", "project6"]
projects79 = ["project7","project8"]

for project in [projects13, projects46,projects79]:
    if len(project) == 1:
        _,col,_ = st.columns([0.33,0.33,0.33])
        columns = [col]
    if len(project) == 2:
        _,left,right,_ = st.columns([0.17,0.33,0.33,0.17])
        columns = [left,right]
    if len(project) == 3:
        columns = st.columns(3)
        
    for col, proj in zip(columns, project):                
        with col:
            st.markdown(f"<button class='myButton'>{proj}</button>", unsafe_allow_html=True)
