Feature: Visualizar vehículo

  Scenario: Visualizar un vehiculo
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Busca Vehiculo a Visualizar PMA-1056

  Scenario: Visualizar un vehiculo en viaje
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Busca Vehiculo a Visualizar ABC-123

  Scenario: Visualizar un vehiculo inexistente
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Busca Vehiculo a Visualizar XDA-123
