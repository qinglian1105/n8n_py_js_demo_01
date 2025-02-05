// n8n_javascript.js

// Format a number with commas
function with_commas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Function for transforming Json data into Html table
function json_to_html_tb(json_obj) {
  let table = "<thead><tr><th>Code</th><th>Name</th><th>Amount(TWD)</th></tr></thead>tr_data"
  let trs = ""
  for (let i = 0; i < json_obj.length; i++) { 
    let col01 = "<td class='scode'>" + json_obj[i].json.s_code + "</td>"
    let col02 = "<td class='sname'>" + json_obj[i].json.s_name + "</td>"
    let col03 = "<td class='amt'>" + with_commas(json_obj[i].json.holding_amount) + "</td>"  
    let row = "<tr>" + col01 + col02 + col03 + "</tr>"    
    trs = trs + row
  } 
  let tb = table.replace("tr_data",trs)
  let html = tb 
  return html;
}

// Get the results of previous node in n8n    
let node_input = $input.all()

let res = {"html_table": json_to_html_tb(node_input)}

// Pass data to next node in n8n
return res;

