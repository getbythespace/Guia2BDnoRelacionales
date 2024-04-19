function drawPokemonChart() {
  d3.json('pokemon.json').then(function(data) {
    var margin = { top: 20, right: 30, bottom: 50, left: 100 }; 
    var width = 800 - margin.left - margin.right;
    var height = 500 - margin.top - margin.bottom;

    var svg = d3.select("#chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var allAbilities = data.flatMap(pokemon => pokemon.abilities);
    var uniqueAbilities = Array.from(new Set(allAbilities));

    var abilities = uniqueAbilities.map(ability => ({
      ability,
      count: data.filter(pokemon => pokemon.abilities.includes(ability)).length
    }));

    var xScale = d3.scaleBand()
      .domain(abilities.map(d => d.ability))
      .range([0, width])
      .padding(0.1);

    var yScale = d3.scaleLinear()
      .domain([0, d3.max(abilities, d => d.count)])
      .range([height, 0]);

    svg.selectAll("rect")
      .data(abilities)
      .enter()
      .append("rect")
      .attr("x", d => xScale(d.ability))
      .attr("y", d => yScale(d.count))
      .attr("width", xScale.bandwidth())
      .attr("height", d => height - yScale(d.count))
      .attr("fill", "steelblue");

    var text = svg.selectAll("text")
      .data(abilities)
      .enter()
      .append("text")
      .text(d => d.ability)
      .attr("x", d => xScale(d.ability) + xScale.bandwidth() / 2)
      .attr("y", d => yScale(d.count) + 20) 
      .attr("text-anchor", "middle")
      .attr("font-size", "14px") 
      .attr("fill", "black");


    text.filter((d, i, nodes) => {
      const yPos = +d3.select(nodes[i]).attr("y");
      return yPos < height;
    }).remove();

    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(xScale))
      .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", ".15em")
      .attr("transform", "rotate(-45)");

    svg.append("g")
      .call(d3.axisLeft(yScale));
  });
}

function drawAbilitiesChart() {
  d3.json('abilities.json').then(function(data) {
    var margin = { top: 20, right: 30, bottom: 50, left: 60 };
    var width = 800 - margin.left - margin.right;
    var height = 500 - margin.top - margin.bottom;

    var svg = d3.select("#abilities")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var abilities = Object.entries(data).map(([ability, count]) => ({ ability, count }));

    var xScale = d3.scaleBand()
      .domain(abilities.map(d => d.ability))
      .range([0, width])
      .padding(0.1);

    var yScale = d3.scaleLinear()
      .domain([0, d3.max(abilities, d => d.count)])
      .range([height, 0]);

    svg.selectAll("rect")
      .data(abilities)
      .enter()
      .append("rect")
      .attr("x", d => xScale(d.ability))
      .attr("y", d => yScale(d.count))
      .attr("width", xScale.bandwidth())
      .attr("height", d => height - yScale(d.count))
      .attr("fill", "lightgreen");

    var text = svg.selectAll("text")
      .data(abilities)
      .enter()
      .append("text")
      .text(d => d.ability)
      .attr("x", d => xScale(d.ability) + xScale.bandwidth() / 2)
      .attr("y", d => yScale(d.count) + 20) 
      .attr("text-anchor", "middle")
      .attr("font-size", "14px") 
      .attr("fill", "black");

    
    text.filter((d, i, nodes) => {
      const yPos = +d3.select(nodes[i]).attr("y");
      return yPos < height;
    }).remove();

    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(xScale))
      .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", ".15em")
      .attr("transform", "rotate(-45)");

    svg.append("g")
      .call(d3.axisLeft(yScale));
  });
}

document.addEventListener('DOMContentLoaded', function() {
  drawPokemonChart();

  drawAbilitiesChart();
});
