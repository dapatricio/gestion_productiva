
//Cargar el API de visualización y el paquete GeoChart.
     google.load('visualization', '1', {'packages': ['geochart']});
     //una devolución de llamada que se ejecutará cuando se carga el API de visualización de Google.
     google.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {
    // se crea un arreglo, donde se indica que la primera linea como se va a particionar el mapa, nombre del estado y tamaño de la población.
        var data = google.visualization.arrayToDataTable([
          ['States','Estado','Discapacidades'], 
          ['EC-A','Azuay',{{Azuay}}],
          ['EC-B','Bolivar',{{Bolivar}}],
          ['EC-F','Cañar',{{Canar}}],
          ['EC-C','Carchi',{{Carchi}}],
          ['EC-H','Chimborazo',{{Chimborazo}}],
          ['EC-X','Cotopaxi',{{Cotopaxi}}],
          ['EC-O','El Oro',{{El_Oro}}],
          ['EC-E','Esmeraldas',{{Esmeraldas}}],
          ['EC-W','Galapagos',{{Galapagos}}],
          ['EC-G','Guayas',{{Guayas}}],
          ['EC-I','Imbabura',{{Imbabura}}],
          ['EC-L','Loja',{{Loja}}],
          ['EC-R','Los Rios',{{Los_Rios}}],
          ['EC-M','Manabi',{{Manabi}}],
          ['EC-S','Morona Santiago',{{Morona_Santiago}}],
          ['EC-N','Napo',{{Napo}}],
          ['EC-D','Orellana',{{Orellana}}],
          ['EC-Y','Pastaza',{{Pastaza}}],
          ['EC-P','Pichincha',{{Pichincha}}],
          ['EC-SE','Santa Elena',{{Santa_Elena}}],
          ['EC-SD','Santo Domingo',{{Santo_Domingo}}],
          ['EC-U','Sucumbios',{{Sucumbios}}],
          ['EC-T','Tungurahua',{{Tungurahua}}],
          ['EC-Z','Zamora Chinchipe',{{Zamora_Chinchipe}}]         
        ]);

    var options = 
    {
        //legend: 'none',  se quita el slider indicador de poblacion minima y maxima
        //tooltip: {trigger:'none'}, 
        region: 'EC',   // region a dibujar en el mapa
        resolution: 'provinces',    //
        //displayMode: 'markers',
        // color minimo: 'LightYellow' y color maximo: 'Salmon', igual se pueden utilizar los valor rgb.
        colorAxis: {colors: ['Green', 'Red', 'Blue', 'yellow', '#FF9C00'] }
    };
    //se instacia y se dibuja el grafico
    var chart = new google.visualization.GeoChart(document.getElementById('chart_div1'));
    chart.draw(data, options);
};


function selecProv(){
        var t = document.getElementById("selProv");
        var selectedText = t.options[t.selectedIndex].value;
        alert("Seleccion: "+selectedText);
    }