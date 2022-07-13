   
$(document).ready(function()
   {
      $("a[href*='#header']").click(function(event)
      {
         event.preventDefault();
         $('html, body').stop().animate({ scrollTop: $('#wb_header').offset().top }, 600, 'easeOutCirc');
      });
      $('#ThemeableMenu1 .dropdown-toggle').dropdown({popperConfig:{placement:'bottom-start',modifiers:{computeStyle:{gpuAcceleration:false}}}});
      $(document).on('click','.ThemeableMenu1-navbar-collapse.show',function(e)
      {
         if ($(e.target).is('a') && ($(e.target).attr('class') != 'dropdown-toggle')) 
         {
            $(this).collapse('hide');
         }
      });
      $("#FileUpload1 :file").on('change', function()
      {
         var input = $(this).parents('.input-group').find(':text');
         input.val($(this).val());
      });
      $("a[href*='#home']").click(function(event)
      {
         event.preventDefault();
         $('html, body').stop().animate({ scrollTop: $('#wb_home').offset().top-88 }, 600, 'easeOutCirc');
      });
      var iOS = !!navigator.platform && /iPad|iPhone|iPod/.test(navigator.platform);
      if (iOS)
      {
         $('#wb_home').css('background-attachment', 'scroll');
      }
   });


   function load_all(){ 
      var form = document.createElement("form");
      form.setAttribute("id", "wb_Form1");   
      var lb = document.createElement("label")
      lb.innerHTML = 'Clied Baker'
      lb.setAttribute("style","left:5%")
      lb.setAttribute("id","Label11")
      var lb1 = document.createElement("label")
      lb1.innerHTML = 'Cliedbakeraccount@email.com'
      lb1.setAttribute("style","top:50%")
      lb1.setAttribute("id","Label13")
      var flex = document.createElement("div")
      var lb2 = document.createElement("label")
      lb2.setAttribute("id","Label12")
      lb2.setAttribute("style","position:sticky;left:100%;top:0%;")
      lb2.innerHTML = '13-Fabuary-2022'    
      var lb3 = document.createElement("label")    
      var lb4 = document.createElement("label")
                 form.appendChild(lb1);
                  form.appendChild(lb) ;
                  form.appendChild(lb2); 
               //   flex.appendChild(lb4);
                  document.getElementsByTagName("body")[0]
                 .appendChild(form);
  }
  function load_all_key(){ 
   var form = document.createElement("form");
   form.setAttribute("id", "wb_Form1");   
   var lb = document.createElement("label")
   var lb1 = document.createElement("label")
   lb1.innerHTML = 'eeeeeesdfds435231BHD!!RREYRYR'
   lb1.setAttribute("style","top:50%")
   lb1.setAttribute("id","Label14")
   var lb2 = document.createElement("label")
   lb2.setAttribute("id","Label11")
   lb2.setAttribute("style","position:absolute;left:5%;top:0%;")
   lb2.innerHTML = '3-May-2022'    
   var flex = document.createElement("div")

   var lb3 = document.createElement("label")
   var lb4 = document.createElement("label")
              form.appendChild(lb1);
              form.appendChild(lb2);

               document.getElementsByTagName("body")[0]
              .appendChild(form);
  }


  function load_all_files(){ 
      var form = document.createElement("form");
      form.setAttribute("id", "wb_Form1");   
      var lb1 = document.createElement("label")
      lb1.innerHTML = 'Clied_Baker_Document'
      lb1.setAttribute("style","top:50%")
      lb1.setAttribute("id","Label13")
      var flex = document.createElement("div")
      var lb2 = document.createElement("label")
      lb2.setAttribute("id","Label12")
      lb2.setAttribute("style","position:sticky;left:100%;top:0%;")
      lb2.innerHTML = '17-Fabuary-2022'    
      var lb3 = document.createElement("label")    
      var lb4 = document.createElement("label")
                 form.appendChild(lb1);
                  form.appendChild(lb2); 
               //   flex.appendChild(lb4);
                  document.getElementsByTagName("body")[0]
                 .appendChild(form);
  }