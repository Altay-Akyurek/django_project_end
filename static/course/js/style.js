var svgTurkeyMap = document.getElementById("svg-turkey-map").getElementsByTagName("path");
var cityName = document.getElementById("city-name");

for (i = 0; i < svgTurkeyMap.length; i++) {

  svgTurkeyMap[i].addEventListener("mousemove", function() {
    cityName.classList.add("show-city-name--active");
    cityName.style.left = (event.clientX + 20 + "px");
    cityName.style.top = (event.clientY + 20 + "px")
    cityName.innerHTML = this.getAttribute("title");
  });

  svgTurkeyMap[i].addEventListener("mouseleave", function() {
    cityName.classList.remove("show-city-name--active");
  });

  
  svgTurkeyMap[i].addEventListener("mouseover", function() {
    if(typeof mapData !== "undefined"){
      let city = this.getAttribute("data-city-name");
      let find = mapData.filter((x) => x.planting_area === city);
      let total = find.length > 0 ? find[0].total : 0;

      let cityOrj = this.getAttribute("city-title");
      this.setAttribute("title", myTooltipTemplate(cityOrj, total));

      new bootstrap.Tooltip(this)
    }
  });

}



const myTooltipTemplate = (city, total) => {
  return `<div class="d-flex flex-column justify-content-center align-items-center text-dark"> 
            <span class="font-weight-bolder fs-6">${city}</span>
            <span class=""> Toplam : <b>${total}</b> </span>
          </div>`;
}