from pyscript import document,display
# Dictionary containing planet information

Elements = {"HYDROGEN": ("Hydrogen",H,1,1.008),"HELIUM": ("Helium",He,2,4.0026),
           "CARBON": ("Carbon",C,6,12.011),"NITROGEN": ("Nitrogen",N,7,14.007),
           "OXYGEN": ("Oxygen",O,8,15.999), "FLUORINE": ("Fluorine",F,9,18.998),
           "PHOSPHORUS": ("Phosphorus",P,15,30.974), "NEON": ("Neon",Ne,10,20.180),
           "SULFUR": ("Sulfur",S,16,32.06), "CHLORINE": ("Chlorine",Cl,17,35.45),
           "ARGON": ("Argon",Ar,18,39.948), "SELENIUM": ("Selenium",Se,34,78.971),
           "BROMINE": ("Bromine",Br,35,79.904), "KRYPTON": ("Krypton",Kr,36,83.798),
           "IODINE": ("Iodine",I,53,126.90), "XENON": ("Xenon",Xe,54,131.29),
           "RADON": ("Radon",Rn,86,222), "OGANESSON": ("Oganesson",Og,118,294)}
#       ELEMENT: ELEMENT NAME, ATOMIC #,
    # KEY : VALUE
    #Element symbol,Element Name,Atomic Number,Atomic Mass ,# of moons
# Function to search for a planet
def search_nonmetals(e):
    # Get the input FROM HTML
    nonmetals1 = document.getElementById("nonmetals1").value.upper()
    # Retrieve information from dictionary 
    result = non_metals.get(Element1, ("Element not found", "-", "-"))
    # Display the result in HTML
    # Element Symbol,Element Name,Atomic Number,Atomic Mass
    document.getElementById("symbol").innerText = Elements
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]
    document.getElementById("mass").innerText = result[3]