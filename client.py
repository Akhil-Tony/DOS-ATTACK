import requests
import time
import streamlit as st

time_interval = 1

def main():
    st.title("DDOS Attack")
    target = st.text_input("select target","http://127.0.0.1:8000")
    option = st.radio("Select the attack", ("Normal", "ddos attack"))
    height = st.text_input("input height")
    weight = st.text_input("input weight")
    
    output = st.empty()
    
    if st.button("Attack"):

        if option == "Normal":
            height = height.split(',')[0]
            weight = weight.split(',')[0]

            response = requests.get(target+'/items/'+str(weight)+'/'+str(height))
            output.write("*request sent for "+str(height)+" "+str(weight)+" *")

        if option == "ddos attack":
            
            height_list = height.split(',')
            weight_list = weight.split(',')
            loop_length = min(len(height_list),len(weight_list))
            i = 0
            while i < loop_length:
                r = requests.get(target+'/items/'+str(weight_list[i])+'/'+str(height_list[i]))
                
                if r.text == 'false':
                    print("breaked")
                    break
                time.sleep(time_interval)
                output.write("*request sent for "+str(weight_list[i])+" "+str(height_list[i])+"  .......*")
                i += 1
                print("requests sent "+str(i))
                if i == loop_length:
                    i = 0
    
if __name__ == "__main__":
    main()
