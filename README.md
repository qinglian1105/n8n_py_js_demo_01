# **n8n_py_js_demo_01**

## **Implementing an example of integrating JavaScript and Python with n8n for Web Automation**

### **Ⅰ. Purpose** 
The content of this project is an experiment of integrating JavaScript and Python with n8n, powerful workflow automation software, for periodically collecting data from website.<br><br>

### **Ⅱ. Tools or Packages**
n8n, Python, Javascript. <br><br>

### **Ⅲ. Statement**
<br>

__1. The data source__ <br>

The data is complaint ranking list of Taichung City in Taiwan and belongs to part of Open Data in Taiwan.<br>
(Please refer to [details](<https://datacenter.taichung.gov.tw/swagger/OpenData/37800d26-6574-4326-be6e-55c765b72f3d>))<br>
<br>

__2. Workflow__ <br>

The workflow of n8n uses several types of node, including "Schedule Trigger", "Execute Command", "Code", "If", and "Gmail". The mainly steps are as below.
<br>
(1)Run python script to call API and save results into CSV file in docker container.<br>
(2)Transform data type with Pyton or JavaScript.<br>
(3)Send message according to different conditions with Gmail.<br>  

![avatar](./README_png/n8n_editor.png)
<br>
<br>

__3. Results__ <br>

As memtioned above, collecting data from website will be saved into CSV file. Then, regardless of whether the node "Transform data type with Python" completes or not, the workflow will send an email to announce recipient.<br>
(Concerning to the details, please refer to the files of this project) <br>

![avatar](./README_png/n8n_executions.png)

<br><br><br>

---

### **Ⅳ. References**

[1] [n8n](<https://n8n.io/>)

[2] [naskio/docker-n8n-python](<https://github.com/naskio/docker-n8n-python/tree/main>)

[3] [Taichung City Government Open Data](<https://opendata.taichung.gov.tw/>)