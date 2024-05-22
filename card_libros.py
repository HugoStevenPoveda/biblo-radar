# Definición del componente personalizado
import streamlit as st





def biblioteca_card_border( autor ,titulo,descripcion):
    st.markdown( f"""
       <div class="card border-info mb-3" style="max-width: 18rem;">
         <div class="card-header">{titulo}</div>
         <div class="card-body">
                <h5 class="card-title">{autor}</h5>
                <p class="card-text">{descripcion}</p>
               
         </div>
      </div>
        """,
        unsafe_allow_html=True
    )




