class AgenteBDI:
    def __init__(self):
        # Crenças sobre o ambiente
        self.crencas = {
            'esta_escuro': False,
            'luz_acesa': False,
            'temperatura': 20  # Inicializando com uma temperatura padrão (20°C)
        }
        
        # Desejos: Manter a casa iluminada e confortável
        self.desejos = {
            'casa_iluminada': True,
            'temperatura_confortavel': (18, 24)  # Definindo o intervalo de temperatura desejada
        }
        
        # Intenções: Ações que o agente vai tomar
        self.intencoes = []

    # Atualiza as crenças com informações do ambiente
    def atualizar_crencas(self, esta_escuro, temperatura):
        self.crencas['esta_escuro'] = esta_escuro
        self.crencas['temperatura'] = temperatura
    
    # Deliberar sobre as intenções com base nas crenças e desejos
    def deliberar(self):
        # Verificar iluminação
        if self.crencas['esta_escuro'] and not self.crencas['luz_acesa']:
            self.intencoes.append('acender_luz')
        elif not self.crencas['esta_escuro'] and self.crencas['luz_acesa']:
            self.intencoes.append('apagar_luz')
        
        # Verificar temperatura
        if self.crencas['temperatura'] < self.desejos['temperatura_confortavel'][0]:
            self.intencoes.append('ligar_aquecimento')
        elif self.crencas['temperatura'] > self.desejos['temperatura_confortavel'][1]:
            self.intencoes.append('ligar_resfriamento')

    # Executar as intenções
    def executar_intencoes(self):
        while self.intencoes:
            intencao = self.intencoes.pop(0)
            if intencao == 'acender_luz':
                print("Luz acesa.")
                self.crencas['luz_acesa'] = True
            elif intencao == 'apagar_luz':
                print("Luz apagada.")
                self.crencas['luz_acesa'] = False
            elif intencao == 'ligar_aquecimento':
                print("Aquecimento ligado.")
            elif intencao == 'ligar_resfriamento':
                print("Resfriamento ligado.")

# Simulação
if __name__ == "__main__":
    agente = AgenteBDI()
    
    # Atualizar crenças com base no ambiente (escurecendo e esfriando)
    agente.atualizar_crencas(esta_escuro=True, temperatura=16)
    
    # Deliberar e executar intenções
    agente.deliberar()
    agente.executar_intencoes()
    
    # Simular nova mudança no ambiente (clareando e aquecendo)
    agente.atualizar_crencas(esta_escuro=False, temperatura=26)
    
    # Deliberar e executar intenções novamente
    agente.deliberar()
    agente.executar_intencoes()
