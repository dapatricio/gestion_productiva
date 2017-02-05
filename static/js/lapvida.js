google.load('visualization', '1.0', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table, 
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Topping');
      data.addColumn('number', 'cantidad');
      data.addRows([
        ['Analfebetismo urbano', 2466],
        ['Alfabetismo Urbano', 24749],
      ]);

// Set chart options
      var options = {'title':'Analfabetismo y Alfabetismo Provincia de Loja'};

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }



    google.load('visualization', '1.0', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChart2);

      // Callback that creates and populates a data table, 
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart2() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Topping');
      data.addColumn('number', 'cantidad');
      data.addRows([
        ['Mental', 1986],
        ['Auditiva', 3801],
        ['Visual', 5832],
        ['Fisico motora', 9299],
        ['Intelectual', 4757]
      ]);

// Set chart options
      var options = {'title':'Discapacidades en la provincia de Loja'};

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('chart_div2'));
      chart.draw(data, options);
    }



    google.load('visualization', '1.0', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChart3);

      // Callback that creates and populates a data table, 
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart3() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Topping');
      data.addColumn('number', 'cantidad');
      data.addRows([
        ['Ninguno', 157],
        ['Centro de Alfabetización/(EBA)', 161],
        ['Preescolar', 3827],
        ['Primario', 510],
        ['Secundario', 716],
        ['Educación Básica', 217],
        ['Bachillerato', 62],
        ['Ciclo Postbachillerato', 211],
        ['Superior', 168]
      ]);

// Set chart options
      var options = {'title':'Nivel educativo alcanzado en la provincia de Loja por individuos con discapacidad intelectual'};

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('chart_div3'));
      chart.draw(data, options);
    }