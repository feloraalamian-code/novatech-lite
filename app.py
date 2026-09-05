import re
import os
import streamlit as st
import json
with open(os.path.join(os.path.dirname(__file__), "products.json"), "r", encoding="utf-8-sig") as file:
    products =json.load(file)

    st.title("novatech sales assistant")
    st.caption("find the perfect laptop for your needs")
    question =st.text_input("ask about a laptop:")
    def find_products(user_question, all_products):
          text= user_question.lower()
          numbers = re.findall( r'\d+', text)
          matches =[]
          for p in all_products:
                for word in p["usage"]:
                      if word in text:
                            matches.append(p)
                            break
          if numbers:
            budget =int(numbers[0])
            matches = [p for p in matches if p["price"] <=budget]
          return matches
    if question:
       results = find_products(question, products)
       if results:
            for r in results:
                st.success(f"{r['name']} _ {r['price']:,} toman\n\n{r['description']}")
       else:
            st.write("No matching product found.")
