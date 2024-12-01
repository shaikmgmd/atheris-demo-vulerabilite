# fuzzer_test.py
import atheris
import sys
import vulnerable
import vulnerable_secure

@atheris.instrument_func
def TesterUneEntree(data):
    try:
        # Conversion des données générées par le fuzzer en chaîne de caractères
        fdp = atheris.FuzzedDataProvider(data)
        chaine_entree = fdp.ConsumeString(24)
        
        # Test de la fonction
        vulnerable.analyser_nom(chaine_entree)
        #vulnerable_secure.analyser_nom_securise(chaine_entree)
    except Exception as e:
        # On ignore les exceptions ValueError qui sont attendues
        if not isinstance(e, ValueError):
            raise

def main():
    atheris.Setup(sys.argv, TesterUneEntree)
    atheris.Fuzz()

if __name__ == "__main__":
    main()

