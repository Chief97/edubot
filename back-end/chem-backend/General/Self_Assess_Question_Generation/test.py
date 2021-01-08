from General.Self_Assess_Question_Generation.FetchImportantSentences import FetchImportantSentences
from General.Self_Assess_Question_Generation.PreProcess import PreProcess


class test(object):
    def __init__(self):
        self.para = ""
        self.value = "";
        self.count = "";




ParaList=[
"To measure the mass of items like a motor car, a brick, a loaf bread, a tea spoonful of sugar and a tablet of medicine, units like kilogram, gram and milligram can be used. But if the mass of very small particles such as a carbon dioxide molecule, or a helium atom is given in units like kilogram or gram, the value obtained is extremely small. Even the attogram (ag), the smallest units of mass is too large to indicate the mass of atoms or ions.",
"For this reason, the mass of a selected atom was taken as a unit and the masses of the other atoms were given relative to it. The mass so expressed is known as the relative atomic mass. The relative atomic mass is not the true mass of an atom of an element. In the past, the mass of an atom of hydrogen, the lightest element was used as the atomic mass unit. The mass of the unit relative to which the masses of other atoms are expressed is  called the atomic mass unit",
"Since many elements are reactive, their atoms do not exist as free atoms. They exist naturally as molecules formed by joining two or more atoms of them. Compounds are composed of molecules formed by the combination of atoms belonging to different elements",
"If the molecular formula of an element or a compound is known, its relative molecular mass can be calculated. This is because the relative molecular mass is equal to the sum of relative atomic masses of the atoms in a molecule. For example a water molecule has two hydrogen atoms (H) and one oxygen atom (O) bound together. Therefore, the relative molecular mass of water (H2O) is the sum of the relative atomic masses of two hydrogen atoms and an oxygen atom. Since the relative atomic mass of hydrogen is 1 and oxygen is 16, the relative molecular mass of water can be calculated as follows.",
"The ionic compounds such as sodium chloride (NaCl) exist as lattices but not molecules. Its formula is written to indicate the simplest ratio in which Na+ and Cl- ions are present in the ionic lattice. In such compounds what is calculated as the relative molecular mass is the mass relevant to their empirical formula. It is known as the relative formula mass or formula mass. When a mass of any element equal to its relative atomic mass is taken in grams, it is seen that it contains the same number of atoms irrespective of the element. Similarly, it can also be shown that when a mass of any substance equal to its relative molecular mass is taken in grams, it contains the same number of molecules. After the great scientist Amedeo Avogadro, this constant number is called Avogadro Constant",
"In various tasks, measurement of the amount of a substance is a requirement. A dozen of books means 12 books. Similarly 'ream' is used to measure the amount of papers. In the SI unit system, the unit used to measure the amount of a substance is the mole. The mole is the amount of a substance that contains as many basic building units (atoms, molecules, ions) as there are atoms in exactly 12.00 g of C – 12 isotope. The number of basic units contained in a mole of any substance is a constant and it is equal to the Avogadro constant or 6.022 x 1023. Thus, the relative atomic mass of any element taken in grams contains one mole of atoms or 6.022 x 1023 atoms. The relative molecular mass of any substance taken in grams contains one mole of molecules or 6.022 x 1023 molecules.",
"A mole of an element or a compound that exists as molecules means a mole of molecules of them. Since mole is a unit that indicates a very large amount, it is not suitable to measure the amount of substances that we come across in day to day life. Therefore, the unit mole is practically used to measure the amounts of things such as atoms, molecules and ions which exist in very large numbers. The following example illustrates the magnitude of the number representing a mole.",
"As the number of units belonging to a mole is very large, counting is impossible. Therefore, other methods are used to measure the mole. One method to have a mole of atoms of an element is weighing out its relative atomic mass in grams. For example, the relative atomic mass of sodium is 23. In order to have a mole of molecules of a given compound, its relative molecular mass has to be weighed out in grams. For instance, the relative molecular mass of glucose (C6H12O6) is 180",
"Molar mass is the mass of a mole of any substance. Though relative atomic mass and relative molecular mass have no units, grams per mole (g mol-1) or kilograms per mole (kg mol-1) is the unit of the molar mass",
"The outermost shell carrying electrons in an atom of an element is known as its valence shell.The valence shell of the atoms of neon and argon has eight electrons each. This electronic structure has been identified as a stable electronic configuration. Because of this stable configuration their reactivity is very low, so they are referred to as noble gases. But, the state of sodium and chlorine atoms is different. In order to have the stable noble gas configuration, a sodium atom has to either lose the electron in the last shell or gain seven electrons. Similarly a chlorine atom can attain the stable electronic configuration by receiving a single electron or by removing seven electrons. In the atoms of these element, electrons in the valence shell reorganise to acquire the stable electronic configuration. That means, loss, gain or sharing of electrons occurs.",
"The attractive forces or binding among the atoms or ions resulted by the rearrangement of electrons in the valence shell for stabilizing the atoms of elements as described above are called chemical bonds. According to the way the participating atoms behave when they chemically bind together, the chemical bonds can be divided into two types.",
"The electronic configuration of the sodium atom is 2, 8, 1. Sodium is an element with low electronegativity. As the number of protons in a sodium atom is equal to the number of electrons, an atom of sodium is electrically neutral (Fig. 10.1). The atom after losing its electron in the outer energy level becomes a sodium ion (Na+) with a charge of +1 (Fig.10.2). An atom after receiving a charge is known as an ion. Since this ion has a positive charge it is called a positive ion or a cation. The chemical properties of an ion is different from that of an atom. Neutral atoms form positively charged ions by losing electrons. Neutral atoms form negatively charged  ions  by  gaining electrons. Some polyatomic  groups too bear positive or negative charges (e.g. NH4+, SO42-  , NO3- ). An ion is an atom or a group of atoms with an  electrical  charge",
"The bonds formed due to the strong electrostatic attractions between the positive and negative ions produced by the exchange of electrons among atoms are known as ionic bonds or electrovalent bonds. So, sodium chloride is a compound with ionic bonds. Such compounds are called ionic compounds",
"Electron sharing between atoms is another method of forming bonds among them. By sharing of electrons like this, the atoms acquire the noble gas configuration. Joining of atoms by sharing electrons between a pair of atoms is referred to as a covalent bond. Sharing of electrons between atoms of the same kind gives rise to homoatomic molecules.",
"Always electrons in the valence shells of atoms participate in the formation of covalent bonds. The Lewis dot and cross diagram illurtrates how electrons exist in the covalent bond. In this diagram, electrons of one atom are represented by dots while the electrons of the other atom are shown by crosses. For example, let's take the dot and cross structure of the methane (CH4) molecule. Carbon whose electronic configuration is 2, 4 has four electrons in its valence shell. These electrons are represented by dots. The electrons of hydrogen atoms which form covalent bonds with carbon are symbolized by the crosses. Showing covalent bonds of a molecule representing the valence shell electrons of its atoms only by dots is called the Lewis dot diagram. The electrons represented by dots are known as lone pairs whereas electrons pairs represented by lines are called bond pairs. The dot and cross diagrams, Lewis dot diagrams and Lewis structures of some covalent molecules are given in Table 10.3.",
"In the ammonia molecules nitrogen atom is the central atom and hydrogen atoms are the peripheral atoms. There are three bond pairs and a single lone pair in the valence shell of the ammonia molecule. In all the molecules given above, the central atom as well as the peripheral atoms have acquired the noble gas configuration. That means, except in hydrogen, a set of eight electrons is completed in the valence shell of atoms after the formation of the bonds. Those are known as the  compounds in which the octet of electrons is complete. Nevertheless, there are exceptions too. Let's take aluminium chloride (AlCl3) as an example. In this, the electronic configuration of the aluminium atom is 2, 8, 3. The electronic configuration of a chlorine atom is 2, 8, 7. Three chlorine atoms share three pairs of electrons with an aluminium atom to form an AlCl3 molecule.",
"In some elements the atoms are organised as a lattice. Such lattices in which the  atoms are covalently bonded are known as atomic lattices. Carbon naturally occurs as two forms of atomic lattices, graphite and diamond. They are known as the allotropic forms of carbon. These two forms differ in the way the carbon atoms form covalent bonds with one another. Generally the melting points and  boiling points  of covalent compounds are low. But in diamond and graphite, the melting point and boiling point are high due to their atomic lattice structure",
"Graphite consists of layers of carbon atoms formed by the joining of one carbon atom with three other carbon atoms by single bonds. These layers are superimposed on one other. The forces holding these layers are weak. Thus one layer can easily slide over the other. Because of this structure, graphite behaves as a lubricant. Diamond is a three dimensional lattice in which every carbon atom forms four single bonds with four other carbon atoms. Diamond is the hardest substance found in nature",
"Electronegativity is the tendency of an atom to attract electrons of a chemical bond towards itself. It takes different values for different atoms. Then hydrogen molecule is formed by the joining of two hydrogen atoms of equal electronegativity by a covalent bond. The distribution of electrons in the bond pair of this molecule is symmetrical. Therefore, the hydrogen is a non – polar molecule. But when two atoms of different electronegativities are joined by a covalent bond, the attraction imposed by the two atoms on the bond pair is different. Let us take hydrogen fluoride molecule as an example. Since fluorine is more electronegative than hydrogen, the bond pair is more displaced towards the fluorine atom. So, the electron distribution is not symmetrical. Consequently the fluorine atom bears a small negative charge. This is known as polarization. However the molecule HF as a whole is a neutral molecule.When two atoms of unequal electronegativities are joined by a covalent bond, it gets polarized due to asymmetric distribution of electrons. Such bonds are called polar covalent bonds.In case where two atoms of similar or slightly different electronegativities are joined by a covalent bond, the bonding electrons between those two atoms distribute symmetrically. Such covalent bonds are referred to as non – polar covalent bonds.In the water molecule, there are four pairs of electrons in the valence shell of its oxygen atom. Of them two pairs are bond pairs and two pairs are lone pairs.When an O – H bond of a water molecule is considered, the bond pair shifts more towards the more electronegative oxygen atom. Thus the molecule is polarized  so that the oxygen atom bears a partial negative charge while the hydrogen atom carries a partial positive charge. Hence water is a compound with polar covalent bonds.",
"In water molecules the hydrogen atoms which bear a very small positive partial charge forms attractive forces with oxygen atoms bearing a very small negative charge of the neighbouring water molecules. This kind of attractions among the molecules are known as intermolecular forces or intermolecular bonds.",
"These intermolecular forces are not as strong as the covalent bonds between the oxygen atoms and the hydrogen atoms in a water molecule. Yet, these intermolecular forces impart many special properties to water. Because of these intermolecular forces, water exists as a liquid at room temperature. In case that there were no intermolecular forces among the water molecules, water is a gas at room temperature.",
"In case (i) above solid naphthalene melted and then turned into a vapour. On the cold surface of the spoon the vapour solidified forming a thin solid layer of naphthalene. When solid naphthalene melted, liquid naphthalene vaporized and naphthalene vapour solidified again, and only the physical state (arrangement of particles) of the given substance changed without giving new substances. Such changes are called physical changes. In the instances from (ii) to (iv), the given substances changed forming new substances. Such changes are known as chemical changes or chemical reactions. Observations such as burning with a flame, evolution of heat, effervescence, change in colour and precipitation can be given as evidences for the occurrence of a chemical reaction.",
"The formation of a new compound by the combination of elements with elements or elements with compounds or compounds with compounds is known as a chemical combination reaction. A chemical equation is the symbolic representation of a chemical reaction using chemical formulae. When writing chemical equations in the standard form, reactants are written on the left hand side and the products on the right hand side. An arrow indicates the direction of a reaction. For a reaction, there may be several reactants as well as several products.",
"It is seen that the lustrous nature of the surface of sodium metal diminishes . We cannot see any noteworthy change in the magnesium ribbon. The reason for the disappearance of the shiny nature of the piece of sodium is that it reacts fast with the components in air. Magnesium does not react fast with the components in air. When burnt in air, metals like sodium and magnesium react with oxygen to form their oxides. When heated in air, the surface of metals like zinc (Zn), iron (Fe) and copper (Cu) becomes dull. Prolonged heating turns them into the oxides. Metals like silver (Ag), platinum (Pt) and gold (Au) are not converted to their oxides.",
"HCl is called hydrogen chloride when it exits as a gas. When hydrogen chloride gas is dissolved in water the solution is called hydrochloric acid. This shows that the rate of reactions of metals with dilute acids differ according to the type of the metal. It is seen that copper metal does not react with dilute hydrochloric acid. Many metals react with dilute sulphuric acid also liberating hydrogen gas.",
"The reactivity shown by metals with oxygen, water and, dilute acids is different from one another. The activity series is built up on the basis of those observations as well as other data. The series obtained by the arrangement of metals in the descending order of their reactivity is referred to as the activity series. The activity series is very important in the studies in chemistry. Activity series is useful to identify the precautions to be taken when storing metals. The metals with high reactivity such as sodium (Na), potassium (K) and calcium (Ca) should be stored in liquids such as kerosene and liquid paraffin.  Because of their high reactivity with air, they react with the components in air if they are kept exposed to air.",
"Activity series is useful to find methods that prevent corrosion of metals. Keeping iron in contact with metals like zinc and magnesium that are more reactive than iron to prevent rusting of iron is an example. Activity series helps select metals to make electrochemical cells. Activity series can be used to decide on the methods suitable for extracting metals. Metals extraction involves the separation of the metal from a natural ore which contains that metal. How the metals occur differs according to their reactivity. Reactive metals such as sodium (Na) and potassium (K) cannot be seen as native metals in the natural environment. They are found as very stable ionic compounds in the environment. In order to extract them, electrolysis, a robust method of extracting metals has to be used. These metals are extracted by the electrolysis of their fused (molten) chloride (to be discussed in Grade 11). The metals of moderate reactivity such as iron (Fe), tin (Sn), zinc (Zn) and lead (Pb) are extracted by reducing their compounds by other elements or compounds. The metals of low reactivity such as Silver (Ag), gold (Au) and platinum (Pt) occur in nature as the native metals mixed with other compounds. They are extracted by the physical methods used to separate the mixtures. Hence, strong extraction methods such as electrolysis are used to extract metals at the top of the activity series. More simpler physical methods are used to extract metals at the bottom of the activity series",
"Iron is a metal placed somewhere in the middle of activity series. Iron is extracted from the iron ore mined from the soil. The main component containing iron in the iron ore is haematite (Fe2O3). The structure used to extract iron is called the blast furnace. This is illustrated in Fig.16.1. It is a special furnace about 60 m high. The raw materials are fed into the furnace from the top while hot air is blown in from the bottom. Heating caused by hot air brings about several reactions inside the furnace giving liquid iron. The temperature range within the blast furnace is 1000 0C – 1900 0C. The raw materials used namely iron ore (Fe2O3), limestone (CaCO3) and coke (C) mixed in the correct proportion and powdered finely are charged from the top of the furnace. Silicon dioxide or silica (SiO2) and aluminum oxide or alumina (Al2O3)    present as impurities in the iron ore react with calcium oxide formed by the    decomposition of limestone giving the slag, a mixture of calcium silicate    (CaSiO3) and calcium aluminate (Ca Al2O4).",
"Gold (Au) is a metal that has longer historical relations with the human race than even iron does. There are evidences for the utilization of gold to make coins, various statues and documents. Now, let us see how this metal is extracted. Gold, which is placed at the bottom of the activity series, does not react with any active component of the atmosphere under normal conditions. Therefore it occurs as the native metal in nature. But it is mixed with other impurities. A certain amount of impurities can be removed by sifting the ore containing gold. The density of gold is very high. Therefore, when the ore is powdered finely and mixed into a drain of water, gold settles down first on the bottom. The metal separated by such physical methods is purified further by various methods.",
"Carbon dioxide is a gas that contributed to the advent of life on Earth. This gas brought the temperature of the Earth’s atmosphere to an optimal level for living organisms and it also acts a raw material for photosynthesis, the process that meets the food requirement of all living beings. Carbon dioxide occurs in a percentage as small as 0.03% by volume in the atmosphere",
"The lime water turns milky because the white calcium carbonate so formed is suspended in water. If more carbon dioxide is passed into the test tube containing the gas suspension, the gas reacts with calcium carbonate forming water  soluble calcium  hydrogen carbonate or calcium bicarbonate [(Ca(HCO3)2.]. Therefore the milkiness of the solution disappears. When carbon dioxide is cooled strongly under high pressure, the gas solidifies. When heated the solid carbon dioxide directly turns into the gas without liquefying, so it does not become a liquid like ice. Therefore solid carbon dioxide is known as dry ice. Since the temperature of dry ice (-770C) is very much lower than that of ice, it is used as a super coolant. Dry ice is largely used in food preservation. It is also used to create artificial rains.",
"Catalysts are the substances that increase the rate of a reaction, without being chemically consumed during the reaction. Given below is an activity to find out the effect of a catalyst on the rate of a chemical reaction. The speed of evolution of gas bubbles is higher in the test tube with manganese dioxide. Manganese dioxide has increased the rate of this reaction. Since the mass of manganese dioxide remains the same, it has not been consumed during the reaction. That is, manganese dioxide has acted as a catalyst for this reaction."

]

sentencesList=[
    [
" But if the mass of very small particles such as a carbon dioxide molecule, or a helium atom is given in units like kilogram or gram, the value obtained is extremely small",
  "Even the attogram (ag), the smallest units of mass is too large to indicate the mass of atoms or ions."
    ],
    [
" The mass so expressed is known as the relative atomic mass",
  " In the past, the mass of an atom of hydrogen, the lightest element was used as the atomic mass unit",
  " The relative atomic mass is not the true mass of an atom of an element",
  " The mass of the unit relative to which the masses of other atoms are expressed is  called the atomic mass unit"
    ],
    [
" They exist naturally as molecules formed by joining two or more atoms of them",
  " Compounds are composed of molecules formed by the combination of atoms belonging to different elements",
  "Since many elements are reactive, their atoms do not exist as free atoms"
    ],
    [
" This is because the relative molecular mass is equal to the sum of relative atomic masses of the atoms in a molecule",
  "If the molecular formula of an element or a compound is known, its relative molecular mass can be calculated",
  " Since the relative atomic mass of hydrogen is 1 and oxygen is 16, the relative molecular mass of water can be calculated as follows"
    ],
    [
        " Similarly, it can also be shown that when a mass of any substance equal to its relative molecular mass is taken in grams, it contains the same number of molecules",
        "In such compounds what is calculated as the relative molecular mass is the mass relevant to their empirical formula",
        " After the great scientist Amedeo Avogadro, this constant number is called Avogadro Constant",
        " It is known as the relative formula mass or formula mass",
        " When a mass of any element equal to its relative atomic mass is taken in grams, it is seen that it contains the same number of atoms irrespective of the element"
    ],
    [
        " The relative molecular mass of any substance taken in grams contains one mole of molecules or 6",
        " Thus, the relative atomic mass of any element taken in grams contains one mole of atoms or 6",
        " In the SI unit system, the unit used to measure the amount of a substance is the mole"
    ],
    [
" Therefore, the unit mole is practically used to measure the amounts of things such as atoms, molecules and ions which exist in very large numbers",
  "A mole of an element or a compound that exists as molecules means a mole of molecules of them"
    ],
    [
" One method to have a mole of atoms of an element is weighing out its relative atomic mass in grams",
  " In order to have a mole of molecules of a given compound, its relative molecular mass has to be weighed out in grams",
    ],
    [
    "Molar mass is the mass of a mole of any substance"
    ],
    [
    "The outermost shell carrying electrons in an atom of an element is known as its valence shell",
    "This electronic structure has been identified as a stable electronic configuration",
    "Because of this stable configuration their reactivity is very low, so they are referred to as noble gases",
    "That means, loss, gain or sharing of electrons occurs"
    ],
    [
        " According to the way the participating atoms behave when they chemically bind together, the chemical bonds can be divided into two types",
        "The attractive forces or binding among the atoms or ions resulted by the rearrangement of electrons in the valence shell for stabilizing the atoms of elements as described above are called chemical bonds"
    ],
    [
        "Since this ion has a positive charge it is called a positive ion or a cation",
        "An atom after receiving a charge is known as an ion",
        "Neutral atoms form negatively charged  ions  by  gaining electrons",
        "Sodium is an element with low electronegativity",
        "An ion is an atom or a group of atoms with an  electrical  charge",
        "Neutral atoms form positively charged ions by losing electrons"
    ],
    [
"The bonds formed due to the strong electrostatic attractions between the positive and negative ions produced by the exchange of electrons among atoms are known as ionic bonds or electrovalent bonds",
  " So, sodium chloride is a compound with ionic bonds",
  " Such compounds are called ionic compounds"
    ],
    [
" Sharing of electrons between atoms of the same kind gives rise to homoatomic molecules",
  "Electron sharing between atoms is another method of forming bonds among them",
  " By sharing of electrons like this, the atoms acquire the noble gas configuration",
  " Joining of atoms by sharing electrons between a pair of atoms is referred to as a covalent bond"
    ],
    [
  "Always electrons in the valence shells of atoms participate in the formation of covalent bonds.",
  " Carbon whose electronic configuration is 2, 4 has four electrons in its valence shell",
  " The electrons of hydrogen atoms which form covalent bonds with carbon are symbolized by the crosses",
  " The Lewis dot and cross diagram illurtrates how electrons exist in the covalent bond",
  " The electrons represented by dots are known as lone pairs whereas electrons pairs represented by lines are called bond pairs",
  " Showing covalent bonds of a molecule representing the valence shell electrons of its atoms only by dots is called the Lewis dot diagram",
  " These electrons are represented by dots"
    ],
    [
" Those are known as the  compounds in which the octet of electrons is complete",
  " Three chlorine atoms share three pairs of electrons with an aluminium atom to form an AlCl3 molecule",
  " The electronic configuration of a chlorine atom is 2, 8, 7",
  " In this, the electronic configuration of the aluminium atom is 2, 8, 3"
    ],
    [
" Such lattices in which the  atoms are covalently bonded are known as atomic lattices",
  " Carbon naturally occurs as two forms of atomic lattices, graphite and diamond",
  " They are known as the allotropic forms of carbon",
  " Generally the melting points and  boiling points  of covalent compounds are low"
    ],
    [
" Diamond is the hardest substance found in nature",
"Because of this structure, graphite behaves as a lubricant.",
"Graphite consists of layers of carbon atoms formed by the joining of one carbon atom with three other carbon atoms by single bonds",
    ],
    [
        "Electronegativity is the tendency of an atom to attract electrons of a chemical bond towards itself.",
" Therefore, the hydrogen is a non – polar molecule",
  " Hence water is a compound with polar covalent bonds",
  " Such bonds are called polar covalent bonds",
  " This is known as polarization",
  " Thus the molecule is polarized  so that the oxygen atom bears a partial negative charge while the hydrogen atom carries a partial positive charge",
  " So, the electron distribution is not symmetrical",
  " Consequently the fluorine atom bears a small negative charge",
  " Such covalent bonds are referred to as non – polar covalent bonds"
    ],
    [
        "In water molecules the hydrogen atoms which bear a very small positive partial charge forms attractive forces with oxygen atoms bearing a very small negative charge of the neighbouring water molecules",
  " This kind of attractions among the molecules are known as intermolecular forces or intermolecular bonds"],
    [
        " Yet, these intermolecular forces impart many special properties to water",
  " Because of these intermolecular forces, water exists as a liquid at room temperature",
  "These intermolecular forces are not as strong as the covalent bonds between the oxygen atoms and the hydrogen atoms in a water molecule",
  " In case that there were no intermolecular forces among the water molecules, water is a gas at room temperature"],
    [
    " Such changes are known as chemical changes or chemical reactions",
     " Such changes are called physical changes"],
    [
        " A chemical equation is the symbolic representation of a chemical reaction using chemical formulae",
        "The formation of a new compound by the combination of elements with elements or elements with compounds or compounds with compounds is known as a chemical combination reaction",
    ],
    [
    " The reason for the disappearance of the shiny nature of the piece of sodium is that it reacts fast with the components in air",
    " Magnesium does not react fast with the components in air",
    " Prolonged heating turns them into the oxides"
    ],
    [
    " This shows that the rate of reactions of metals with dilute acids differ according to the type of the metal",
    " Many metals react with dilute sulphuric acid also liberating hydrogen gas",
    "HCl is called hydrogen chloride when it exits as a gas",
    " When hydrogen chloride gas is dissolved in water the solution is called hydrochloric acid",
    " It is seen that copper metal does not react with dilute hydrochloric acid"
    ],
    [
    " The series obtained by the arrangement of metals in the descending order of their reactivity is referred to as the activity series",
    " Activity series is useful to identify the precautions to be taken when storing metals",
    " Because of their high reactivity with air, they react with the components in air if they are kept exposed to air"],
    [
    "Activity series is useful to find methods that prevent corrosion of metals.",
    " Activity series helps select metals to make electrochemical cells",
    " Activity series can be used to decide on the methods suitable for extracting metals",
    " Hence, strong extraction methods such as electrolysis are used to extract metals at the top of the activity series",
    " How the metals occur differs according to their reactivity",
    " They are extracted by the physical methods used to separate the mixtures"
    ],
    ["Iron is extracted from the iron ore mined from the soil",
     "The main component containing iron in the iron ore is haematite (Fe2O3).",
     "The structure used to extract iron is called the blast furnace.",
     "Heating caused by hot air brings about several reactions inside the furnace giving liquid iron.",
     "The temperature range within the blast furnace is 1000 0C – 1900 0C."
    ],
    [
    "Therefore it occurs as the native metal in nature.",
     "A certain amount of impurities can be removed by sifting the ore containing gold.",
     "The density of gold is very high.",
     "Therefore, when the ore is powdered finely and mixed into a drain of water, gold settles down first on the bottom."
    ],
    [
        "This gas brought the temperature of the Earth’s atmosphere to an optimal level for living organisms and it also acts a raw material for photosynthesis, the process that meets the food requirement of all living beings",
        "Carbon dioxide occurs in a percentage as small as 0.03% by volume in the atmosphere."
    ],

    [
    " It is also used to create artificial rains",
    " Dry ice is largely used in food preservation",
    " Therefore solid carbon dioxide is known as dry ice",
    " When carbon dioxide is cooled strongly under high pressure, the gas solidifies",
    " Therefore the milkiness of the solution disappears",
    "The lime water turns milky because the white calcium carbonate so formed is suspended in water"
    ],
    [
    "Catalysts are the substances that increase the rate of a reaction, without being chemically consumed during the reaction.",
    "The speed of evolution of gas bubbles is higher in the test tube with manganese dioxide.",
    "Manganese dioxide has increased the rate of this reaction.",
    "Since the mass of manganese dioxide remains the same, it has not been consumed during the reaction."
    ]
]
results = []
# for x in range(50):
#     # count = 0
#     for i in range(len(ParaList)):
#         print("PARA ", str(i))
#         print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
#         preProcess = PreProcess()
#         pretext = preProcess.preProcessPara(ParaList[i])
#         # print(pretext)
#         fetchImportantSentences = FetchImportantSentences();
#         finalText = fetchImportantSentences.testImportantSentences(pretext,x+1);
#         Text = set(finalText);
#         count = 1
#         for l in Text:
#             if l in sentencesList[i]:
#                 count += 1
#                 print(l)
#         t = test()
#         t.para = i
#         t.value = x+1
#         t.count = count
#         results.append(t)

text11="To measure the mass of items like a motor car, a brick, a loaf bread, a tea spoonful of sugar and a tablet of medicine, units like kilogram, gram and milligram can be used. But if the mass of very small particles such as a carbon dioxide molecule, or a helium atom is given in units like kilogram or gram, the value obtained is extremely small. Even the attogram (ag), the smallest units of mass is too large to indicate the mass of atoms or ions."

#checking for important sentences
for v in range(20):
    # print(v+1)
    count = 0
    preProcess = PreProcess()
    pretext = preProcess.preProcessPara(ParaList[0])
    # print(pretext)
    fetchImportantSentences = FetchImportantSentences();
    finalText = fetchImportantSentences.testImportantSentences(pretext, v+1);
    Text = set(finalText);
    # print(Text)
    for l in Text:
        print(l)
        # print("")
        if l not in sentencesList[0]:
            count += 1
            # print(l)


    print("VALUE : ", str(v+1))
    print("COUNT NEEDED : ", count)
    print("")
    t = test()
    t.para = 32
    t.value = v+1
    t.count = count
    results.append(t)

#checking for no of unimportant sentences selected
for v in range(20):
    # print(v+1)
    count = 0
    preProcess = PreProcess()
    pretext = preProcess.preProcessPara(ParaList[0])
    # print(pretext)
    fetchImportantSentences = FetchImportantSentences();
    finalText = fetchImportantSentences.testImportantSentences(pretext, v+1);
    Text = set(finalText);
    # print(Text)
    for l in Text:
        print(l)
        # print("")
        if l in sentencesList[0]:
            count += 1
            # print(l)


    print("VALUE : ", str(v+1))
    print("COUNT NEEDED : ", count)
    print("")
    t = test()
    t.para = 32
    t.value = v+1
    t.count = count
    results.append(t)

print("-------------------------------------------------------------")
print("SENTENCES LIST LENGTH : ", str(len(sentencesList[0])))
print("")
count = 0
maxcount =count
maxVal= count
for t in results:

    if t.count > maxcount:
        maxcount = t.count
        maxVal = t.value

    print("PARA :" ,str(t.para))
    print("VALUE :" ,str(t.value))
    print("COUNT :" ,str(t.count))
    print("")

print("MAX VAL: ", str(maxVal))
print("MAX COUNT: ",str(maxcount) )