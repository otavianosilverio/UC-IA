import time

if __name__ == "__main__":
    agente = AgenteBDI()

    # Ciclo contínuo de percepção-deliberação-ação
    for _ in range(5):  # Simular 5 iterações
        # Atualização simulada do ambiente (alterna entre dia/noite e temperaturas)
        esta_escuro = not agente.crencas['esta_escuro']
        temperatura = agente.crencas['temperatura'] + (2 if not esta_escuro else -2)
        
        agente.atualizar_crencas(esta_escuro=esta_escuro, temperatura=temperatura)
        
        # Deliberar e executar intenções
        agente.deliberar()
        agente.executar_intencoes()
        
        # Simular intervalo de tempo
        time.sleep(1)
