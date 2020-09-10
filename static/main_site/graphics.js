const svgC = d3.select(".container")
.append("svg")
.attr("height", 500)
.attr("width", 500)

for (i=0;i<5;i++) {
  svgC.append("rect")
  .attr("height", 20)
  .attr("width", 20)
  .attr("x", ()=> {return i*30})
  .attr("y", 20)
}
