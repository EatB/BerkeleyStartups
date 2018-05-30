function toggleCompanyTypeDropDown(){
  var myDropdown = document.getElementById("myDropdown");

  if (myDropdown.classList.contains('show')) {
    myDropdown.classList.remove('show');
  } else{
    myDropdown.classList.toggle('show');
  }
}
function toggleSliderDropDown() {
  console.log("toggling slider");
  var mySlider = document.getElementById("mySlider");
  if (mySlider.classList.contains('show')) {
    mySlider.classList.remove('show');
  } else{
    mySlider.classList.add('show');
  }
}

function changeSliderValue(){
  var slider = document.getElementById("slider");
  var output = document.getElementById("output");
  output.innerHTML = slider.value;
}

window.onclick = function(e){
  var class_list = e.target.classList;
  // toggle dropdowns
  if(class_list.contains('company_type_toggle')) {
    toggleCompanyTypeDropDown();
  } else if(class_list[0] == 'slider_toggle') {
    toggleSliderDropDown();
  } else if(!(class_list[0] == 'tag_choice' || class_list[0] == 'slider')) {
    var mySlider = document.getElementById("mySlider");
    var myDropdown = document.getElementById("myDropdown");
    mySlider.remove('show');
    myDropdown.remove('show');
  }
  //change slider value
  if(class_list[0] == 'slider'){
    changeSliderValue();
  }
}
