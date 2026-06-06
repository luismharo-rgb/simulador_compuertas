#include <stdio.h>

int main() {
    int nota;
    int asistencia;

    printf("--- Validador de Exoneracion ---\n");
    
    printf("Ingresa la nota (1-10): ");
    scanf("%d", &nota);
    
    printf("Ingresa el porcentaje de asistencia (0-100): ");
    scanf("%d", &asistencia);

    // p = (nota >= 8), q = (asistencia >= 80)
    int exonera = (nota >= 8) && (asistencia >= 80);

    // --- EVALUACIÓN DETALLADA ---
    if (exonera) { 
        printf("\n[ESTADO]: EXONERA. ¡Excelente trabajo!");
    } 
    // Caso 1: Fallan ambas (Prioridad alta para diagnóstico completo)
    else if (nota < 8 && asistencia < 80) {  
        printf("\n[RESULTADO]: NO EXONERA. Fallaste en nota y asistencia.");
    }
    // Caso 2: Solo falla la nota
    else if (nota < 8) {  
        printf("\n[RESULTADO]: NO EXONERA por nota insuficiente.");
    } 
    // Caso 3: Solo falla la asistencia
    // (Si llegamos aquí, sabemos que la nota es >= 8 porque los de arriba fallaron)
    else {  
        printf("\n[RESULTADO]: NO EXONERA por falta de asistencia.");
    } 

    printf("\n\nValor logico final: %d", exonera);
    
    printf("\n\nPresiona Enter para salir...");
    getchar(); 
    getchar(); 
    return 0;
}