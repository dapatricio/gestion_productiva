google.load('visualization', '1.0', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChartAnios);

      // Callback that creates and populates a data table, 
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChartAnios() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Topping');
      data.addColumn('number', 'cantidad');
      data.addRows([
        ['Ninguno', {{ninguno}}],
        ['Centro de Alfabetización/(EBA)', {{centro}}],
        ['Preescolar', {{preescolar}}],
        ['Primario', {{primario}}],
        ['Secundario', {{secundario}}],
        ['Educación Básica', {{basica}}],
        ['Bachillerato', {{bachillerato}}],
        ['Ciclo Postbachillerato', {{postbachillerato}}],
        ['Superior', {{superior}}]
      ]);

// Set chart options
      var options = {'title':'Nivel educativo alcanzado en la provincia de  por individuos con discapacidad'};

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('chart_divAnios'));
      chart.draw(data, options);
    }