   
  //fetch('http://127.0.0.1:9090/ShipStore/login/',
  fetch('../../ShipStore/login/Data',
  {method: "GET",
  headers: {
      'X-Requested-With':'XMLHttpRequest',
  }}

)
.then(response => response.json())
.then(data => {
    //console.log(data);
    for (i in data ){
      var form = document.createElement("form");
      form.setAttribute("id", "wb_Form1");   
      var lb = document.createElement("label")
      lb.innerHTML = data[i]['Full_Name']
      lb.setAttribute("style","left:5%")
      lb.setAttribute("id","Label11")
      var lb1 = document.createElement("label")
      lb1.innerHTML = data[i]['Email']
      lb1.setAttribute("style","top:50%")
      lb1.setAttribute("id","Label13")
      var flex = document.createElement("div")
      var lb2 = document.createElement("label")
      lb2.setAttribute("id","Label12")
      lb2.setAttribute("style","position:sticky;left:100%;top:0%;")
      lb2.innerHTML = data[i]['date']    
      var lb3 = document.createElement("label")    
      var lb4 = document.createElement("label")
                 form.appendChild(lb1);
                  form.appendChild(lb) ;
                  form.appendChild(lb2); 
               //   flex.appendChild(lb4);
                  document.getElementsByClassName("new")[0]
                 .appendChild(form);
    }
 
});
   
//=============================================================================
  //fetch('http://127.0.0.1:9090/ShipStore/login/',
  fetch('../../ShipStore/Admin_login/pass_key/ ',
  
  {method: "GET",
  headers: {
      'X-Requested-With':'XMLHttpRequest',
  }}

)
.then(response => response.json())
.then(data => {
    //console.log(data[0]);
    for (i in data ){
      var form = document.createElement("form");
      form.setAttribute("id", "wb_Form1");   
      var lb = document.createElement("label")
      var lb1 = document.createElement("label")
      lb1.innerHTML = data[i]['Key_value']
      lb1.setAttribute("style","top:50%")
      lb1.setAttribute("id","Label14")
      var lb2 = document.createElement("label")
      lb2.setAttribute("id","Label16")
     // lb2.setAttribute("style","left:5%;top:0%;")
      lb2.innerHTML = data[i]['date']     
      var flex = document.createElement("div")
      var lb3 = document.createElement("label")
      var lb4 = document.createElement("label")
              form.appendChild(lb1);
              form.appendChild(lb2);
               document.getElementsByClassName("new2")[0]
              .appendChild(form);
    }
 
});

//==============================================================================================
   

fetch('../../ShipStore/Admin_login/Upload/Data ',
  
{method: "GET",
headers: {
    'X-Requested-With':'XMLHttpRequest',
}}

)
.then(response => response.json())
.then(data => {

  console.log(data);
  for (i in data ){
   var name_link = data[i][1] 
   console.log(name_link);
    
   var form = document.createElement("form");
      form.setAttribute("id", "wb_Form1"); 
      form.setAttribute("name", name_link ); 
      form.addEventListener('click',function(){
         console.log(this.name);
         load_all_files(this.name)
          
      }) 
     
      var lb1 = document.createElement("label")
      lb1.innerHTML = data[i][1]
      lb1.setAttribute("style","top:50%")
      lb1.setAttribute("id","Label13")

      var flex = document.createElement("div")
      var lb2 = document.createElement("label")
      lb2.setAttribute("id","Label12")
      lb2.setAttribute("style","position:sticky;left:100%;top:0%;")
      lb2.innerHTML = data[i][2]    
      var lb3 = document.createElement("label")    
      var lb4 = document.createElement("label")
                 form.appendChild(lb1);
                  form.appendChild(lb2); 
               //   flex.appendChild(lb4);

                  document.getElementsByClassName("new3")[0]
                 .appendChild(form);
  }

});

  function load_all_files(data){ 
      window.open('../media/'+data);
  }