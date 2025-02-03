// n8n_javascript.js

function processing_data(jstr) {
  const int_cols = ["編號", "件數"];
  const float_cols = ["該業務占排名前十大百分比"];
  let obj_list = JSON.parse(jstr);
  for (let i = 0; i < obj_list.length; i++) {
    obj_list[i][int_cols[0]] = parseInt(obj_list[i][int_cols[0]]);
    obj_list[i][int_cols[1]] = parseInt(obj_list[i][int_cols[1]]);
    obj_list[i][float_cols[0]] = parseFloat(obj_list[i][float_cols[0]]);
  }
  return obj_list;
}

//  Get the results of previous node in n8n
let jstr = $input.first().json.stdout;

let ds = processing_data(jstr);

//  Pass data to next node in n8n
return ds;
