from eventos import EventoUnico, EventoRecorrente

print("=== Teste EventoUnico ===")
evento = EventoUnico("Reunião", "Sala 302, prédio da esquina", "05/10/2023, 16:30")
print(evento)

evento.editar_data_hora("05/10/2024, 16:30")
print(evento)

print("\n=== Teste EventoRecorrente ===")
eventos = EventoRecorrente(
    "Reunião Mensal",
    "Sala 302, prédio da esquina",
    "05/01/2024, 16:30",
    "05/01/2025, 16:30",
    30
)

print(eventos)

eventos.editar_data_hora("05/12/2024, 16:30", "05/12/2024, 11:30")
print("\nApós editar:")
print(eventos)

print("\n=== Teste de Polimorfismo ===")
lista_eventos = [
    EventoUnico("Consulta", "Médico", "01/02/2024, 09:00"),
    EventoUnico("Aula", "Matemática", "10/03/2024, 08:00"),
    eventos  # EventoRecorrente
]

for e in lista_eventos:
    print("\n", e)
