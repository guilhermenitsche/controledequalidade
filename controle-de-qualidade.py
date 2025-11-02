

# ============================================
# CRITÉRIOS DE QUALIDADE
# ============================================
PESO_MIN = 95
PESO_MAX = 105
CORES_VALIDAS = ['azul', 'verde']
COMPRIMENTO_MIN = 10
COMPRIMENTO_MAX = 20
CAPACIDADE_CAIXA = 10

# ============================================
# ARMAZENAMENTO DE DADOS
# ============================================
todas_pecas = []
pecas_aprovadas = []
pecas_reprovadas = []
caixas = [[]]  # Lista de caixas (cada caixa é uma lista)

# ============================================
# FUNÇÕES DO MENU
# ============================================

def limpar_tela():
    """Simula limpeza de tela"""
    print("\n" * 2)

def exibir_cabecalho():
    """Exibe o cabeçalho do sistema"""
    print("="*60)
    print("    SISTEMA DE CONTROLE DE QUALIDADE INDUSTRIAL")
    print("="*60)
    print(f"Critérios: Peso {PESO_MIN}-{PESO_MAX}g | Cor: {'/'.join(CORES_VALIDAS)} | Comp: {COMPRIMENTO_MIN}-{COMPRIMENTO_MAX}cm")
    print("="*60)

def exibir_menu():
    """Exibe o menu principal"""
    print("\n📋 MENU PRINCIPAL")
    print("-" * 60)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair do sistema")
    print("-" * 60)

def cadastrar_peca():
    """Opção 1: Cadastrar nova peça"""
    print("\n➕ CADASTRAR NOVA PEÇA")
    print("-" * 60)
    
    # Solicitar dados da peça
    id_peca = input("ID da peça: ").strip()
    
    if not id_peca:
        print("❌ ID não pode ser vazio!")
        input("\nPressione ENTER para continuar...")
        return
    
    # Verificar se ID já existe
    for peca in todas_pecas:
        if peca['id'] == id_peca:
            print(f"❌ Peça com ID '{id_peca}' já existe!")
            input("\nPressione ENTER para continuar...")
            return
    
    try:
        peso = float(input("Peso (g): "))
        cor = input("Cor: ").strip().lower()
        comprimento = float(input("Comprimento (cm): "))
    except ValueError:
        print("❌ Valores numéricos inválidos!")
        input("\nPressione ENTER para continuar...")
        return
    
    # Inspecionar peça
    motivos_reprovacao = []
    
    if peso < PESO_MIN or peso > PESO_MAX:
        motivos_reprovacao.append(f"Peso fora do padrão ({peso}g)")
    
    if cor not in CORES_VALIDAS:
        motivos_reprovacao.append(f"Cor inválida ('{cor}')")
    
    if comprimento < COMPRIMENTO_MIN or comprimento > COMPRIMENTO_MAX:
        motivos_reprovacao.append(f"Comprimento fora do padrão ({comprimento}cm)")
    
    aprovada = len(motivos_reprovacao) == 0
    
    # Criar registro da peça
    peca_completa = {
        'id': id_peca,
        'peso': peso,
        'cor': cor,
        'comprimento': comprimento,
        'aprovada': aprovada,
        'motivos': motivos_reprovacao
    }
    
    # Adicionar às listas
    todas_pecas.append(peca_completa)
    
    print("\n" + "="*60)
    if aprovada:
        print(f"✅ PEÇA APROVADA!")
        pecas_aprovadas.append(peca_completa)
        
        # Adicionar à caixa
        caixa_atual = caixas[-1]
        
        if len(caixa_atual) < CAPACIDADE_CAIXA:
            caixa_atual.append(peca_completa)
            print(f"📦 Adicionada à Caixa {len(caixas)} ({len(caixa_atual)}/{CAPACIDADE_CAIXA} peças)")
        else:
            print(f"📦 Caixa {len(caixas)} FECHADA!")
            caixas.append([peca_completa])
            print(f"📦 Nova Caixa {len(caixas)} iniciada (1/{CAPACIDADE_CAIXA} peças)")
    else:
        print(f"❌ PEÇA REPROVADA!")
        print("\nMotivos:")
        for motivo in motivos_reprovacao:
            print(f"  • {motivo}")
        pecas_reprovadas.append(peca_completa)
    
    print("="*60)
    input("\nPressione ENTER para continuar...")

def listar_pecas():
    """Opção 2: Listar peças aprovadas/reprovadas"""
    print("\n📊 LISTAR PEÇAS")
    print("-" * 60)
    print("1. Listar peças aprovadas")
    print("2. Listar peças reprovadas")
    print("3. Listar todas as peças")
    print("-" * 60)
    
    opcao = input("Escolha uma opção: ").strip()
    
    print("\n" + "="*60)
    
    if opcao == "1":
        print(f"✅ PEÇAS APROVADAS ({len(pecas_aprovadas)} peças)")
        print("="*60)
        if len(pecas_aprovadas) == 0:
            print("Nenhuma peça aprovada.")
        else:
            for peca in pecas_aprovadas:
                print(f"\nID: {peca['id']}")
                print(f"  Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
    
    elif opcao == "2":
        print(f"❌ PEÇAS REPROVADAS ({len(pecas_reprovadas)} peças)")
        print("="*60)
        if len(pecas_reprovadas) == 0:
            print("Nenhuma peça reprovada.")
        else:
            for peca in pecas_reprovadas:
                print(f"\nID: {peca['id']}")
                print(f"  Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
                print("  Motivos:")
                for motivo in peca['motivos']:
                    print(f"    • {motivo}")
    
    elif opcao == "3":
        print(f"📋 TODAS AS PEÇAS ({len(todas_pecas)} peças)")
        print("="*60)
        if len(todas_pecas) == 0:
            print("Nenhuma peça cadastrada.")
        else:
            for peca in todas_pecas:
                status = "✅ APROVADA" if peca['aprovada'] else "❌ REPROVADA"
                print(f"\nID: {peca['id']} - {status}")
                print(f"  Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
    else:
        print("❌ Opção inválida!")
    
    print("="*60)
    input("\nPressione ENTER para continuar...")

def remover_peca():
    """Opção 3: Remover peça cadastrada"""
    print("\n🗑️  REMOVER PEÇA")
    print("-" * 60)
    
    if len(todas_pecas) == 0:
        print("❌ Nenhuma peça cadastrada para remover!")
        input("\nPressione ENTER para continuar...")
        return
    
    print("Peças cadastradas:")
    for i, peca in enumerate(todas_pecas, 1):
        status = "✅" if peca['aprovada'] else "❌"
        print(f"{i}. {peca['id']} {status}")
    
    print("-" * 60)
    id_remover = input("Digite o ID da peça a remover: ").strip()
    
    # Buscar peça
    peca_encontrada = None
    indice = -1
    
    for i, peca in enumerate(todas_pecas):
        if peca['id'] == id_remover:
            peca_encontrada = peca
            indice = i
            break
    
    if peca_encontrada is None:
        print(f"❌ Peça '{id_remover}' não encontrada!")
        input("\nPressione ENTER para continuar...")
        return
    
    # Confirmar remoção
    print(f"\n⚠️  Deseja realmente remover a peça '{id_remover}'? (s/n): ", end="")
    confirmacao = input().strip().lower()
    
    if confirmacao == 's':
        # Remover das listas
        todas_pecas.pop(indice)
        
        if peca_encontrada['aprovada']:
            pecas_aprovadas.remove(peca_encontrada)
            # Remover das caixas e reorganizar
            for caixa in caixas:
                if peca_encontrada in caixa:
                    caixa.remove(peca_encontrada)
                    break
        else:
            pecas_reprovadas.remove(peca_encontrada)
        
        print(f"✅ Peça '{id_remover}' removida com sucesso!")
    else:
        print("❌ Remoção cancelada.")
    
    input("\nPressione ENTER para continuar...")

def listar_caixas_fechadas():
    """Opção 4: Listar caixas fechadas"""
    print("\n📦 CAIXAS FECHADAS")
    print("="*60)
    
    caixas_fechadas = [c for c in caixas if len(c) == CAPACIDADE_CAIXA]
    
    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa fechada ainda.")
    else:
        print(f"Total de caixas fechadas: {len(caixas_fechadas)}\n")
        
        contador = 1
        for i, caixa in enumerate(caixas, 1):
            if len(caixa) == CAPACIDADE_CAIXA:
                print(f"Caixa {contador} (Original: Caixa {i}):")
                print(f"  Status: FECHADA ({CAPACIDADE_CAIXA}/{CAPACIDADE_CAIXA} peças)")
                ids = [p['id'] for p in caixa]
                print(f"  Peças: {', '.join(ids)}")
                print()
                contador += 1
    
    print("="*60)
    input("\nPressione ENTER para continuar...")

def gerar_relatorio():
    """Opção 5: Gerar relatório final"""
    print("\n📄 RELATÓRIO FINAL")
    print("="*60)
    
    # Estatísticas gerais
    total_pecas = len(todas_pecas)
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    
    print(f"\n📊 ESTATÍSTICAS GERAIS")
    print("-" * 60)
    print(f"Total de peças processadas: {total_pecas}")
    print(f"Peças aprovadas: {total_aprovadas}")
    print(f"Peças reprovadas: {total_reprovadas}")
    
    if total_pecas > 0:
        taxa_aprovacao = (total_aprovadas / total_pecas) * 100
        taxa_reprovacao = (total_reprovadas / total_pecas) * 100
        print(f"Taxa de aprovação: {taxa_aprovacao:.1f}%")
        print(f"Taxa de reprovação: {taxa_reprovacao:.1f}%")
    
    # Detalhamento de reprovações
    if total_reprovadas > 0:
        print(f"\n❌ DETALHAMENTO DAS REPROVAÇÕES")
        print("-" * 60)
        for peca in pecas_reprovadas:
            print(f"\nID: {peca['id']}")
            print(f"  Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
            print("  Motivos:")
            for motivo in peca['motivos']:
                print(f"    • {motivo}")
    
    # Informações sobre caixas
    caixas_fechadas = len([c for c in caixas if len(c) == CAPACIDADE_CAIXA])
    caixa_atual = caixas[-1] if len(caixas) > 0 else []
    
    print(f"\n📦 INFORMAÇÕES SOBRE EMPACOTAMENTO")
    print("-" * 60)
    print(f"Total de caixas: {len(caixas)}")
    print(f"Caixas fechadas: {caixas_fechadas}")
    print(f"Caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças")
    
    # Detalhamento das caixas
    if len(caixas) > 0:
        print("\nDetalhamento:")
        for i, caixa in enumerate(caixas, 1):
            status = "FECHADA" if len(caixa) == CAPACIDADE_CAIXA else "EM USO"
            ids = [p['id'] for p in caixa]
            print(f"  Caixa {i}: {len(caixa)}/{CAPACIDADE_CAIXA} peças - {status}")
            if len(ids) > 0:
                print(f"    Peças: {', '.join(ids)}")
    
    print("\n" + "="*60)
    input("\nPressione ENTER para continuar...")

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Função principal do sistema"""
    
    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("\n" + "="*60)
            print("Encerrando sistema... Até logo!")
            print("="*60)
            break
        else:
            print("\
                 Opção inválida! Tente novamente.")
            input("\nPressione ENTER para continuar...")

# Iniciar o sistema
if __name__ == "__main__":
    main()