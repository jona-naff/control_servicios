function cambiaMunicipios(estadoid) {
    $.ajax({
      url:"/products/municipios/" + estadoid,
      type:"get",
      datatype:"html",
      success: function(response) {
          municipios = Array();
          municipios = response["estados"];
          numero_municipios = response["estados"].length;
          html = "<select id=\"selectMunicipios\" onchange=\"cambiaColonia(this.value)\">";
          html += "<option value=0>Selecciona un municipio</option>";
          contador_municipios = 0;
          while (contador_municipios < numero_municipios) {
            html += "<option value="+municipios[contador_municipios]["municipioid"]+">"+municipios[contador_municipios]["nombre"]+"</option>";
            contador_municipios += 1;
            
          }
          html += "</select>";
          $("#sel_municipios").html(html);

          
      },
      error: function(error) {
          console.log(error);
      }
    });
  }

  function cambiaColonia(municipioid) {
    $.ajax({
      url:"/products/colonias/" + municipioid,
      type:"get",
      datatype:"html",
      success: function(response) {
          colonias = Array();
          colonias = response["municipios"];
          numero_colonias = response["municipios"].length;
          console.log(colonias);
      
     
          html = "<select id=\"selectColonias\">";
          html += "<option value=0>Selecciona una colonia</option>";
          contador_colonias = 0;
          while (contador_colonias < numero_colonias) {
            html += "<option value="+colonias[contador_colonias]["coloniaid"]+">"+colonias[contador_colonias]["nombre"]+"</option>";
            contador_colonias += 1;
            
          }
          html += "</select>";
          $("#sel_colonias").html(html);

          
      },
      error: function(error) {
          console.log(error);
      }
    });

  } 

