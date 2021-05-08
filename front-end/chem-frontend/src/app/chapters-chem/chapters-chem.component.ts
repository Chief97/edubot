import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chapters-chem',
  template: `
    <section class="setlist">
      <article class="set">
        <h1 style="color:#89CFF0;font-size: 25px">Electro Chemical Cells</h1>
        <div class="content">
          <div class="definition">
            <p>
              In our everyday life, we frequently use equipment powered by domestic electricity as well as appliances
              operated by electrochemical cells or batteries. Toy cars, electric torches, calculators, computers and
              mobile phones are a few examples for equipment that are powered by electrochemical cells.
            </p>
          </div>
          <br>
          <div class="images">
            <img src="../../assets/images/electro-chemical-cells/figure_12.1.1_toy-car.png"
                 style="width:200px;height:100px;">
            <img src="../../assets/images/electro-chemical-cells/figure_12.1.1_electric-torch.png"
                 style="width:200px;height:100px;">
            <img src="../../assets/images/electro-chemical-cells/figure_12.1.1_mobile-phone.png"
                 style="width:100px;height:200px;">
            <img src="../../assets/images/electro-chemical-cells/figure_12.1.1_calculator.png"
                 style="width:200px;height:200px;">
            <img src="../../assets/images/electro-chemical-cells/figure_12.1.1_computer.png"
                 style="width:200px;height:150px;"><br>
          </div>
          <p>
            The electrochemical cells or batteries used in the examples given above are small in size.
            A battery used to start a car is large in size. Such a battery is a collection of several
            electrochemical cells.<br>
          </p>
          <div class="images">
            <img src="../../assets/images/electro-chemical-cells/figure_12.1.2_types-of-batteries.png"
                 style="width:800px;height:150px;"><br>
          </div>
          <p>
            In your former grades you have learnt about electrochemical cells. In those cells, the chemical
            energy stored in the chemicals they contain is converted to electrical energy. In this section,
            we study further the reactions occurring in electrochemical cells and the action of those cells.<br>
          </p>
          <br>
          <div class="activity">
            For this, let us do the activity 12.1.1 described below.<br>
            <div class="images">
              <img src="../../assets/images/electro-chemical-cells/activity_12.1.1.png">
            </div>
            <br>
            Here, it can be observed that, gas bubbles are liberated near the zinc strip and the zinc strip
            dissolves gradually. Let us find the reasons for those observations.<br>
            Zinc atoms (Zn) go into the solution as zinc ions (Zn<sup>2+</sup>) leaving electrons on the metal.
            Electrons get accumulated on the zinc strip. This process can be shown as follows using chemical
            symbols.<br>
            <br>
            Zn (s)&rarr;Zn<sup>2+</sup>(aq) + 2e&#x21E2;&#x2460;<br>
            <br>
            Sulphuric acid dissociates into hydrogen ions (H<sup>+</sup>) and sulphate ions (SO<sub>4</sub><sup>2-</sup>)
            in
            water. This can be illustrated as follows.<br>
            <br>
            H<sub>2</sub>SO<sub>4</sub>(aq)&rarr;2H<sup>+</sup>(aq) + SO<sub>4</sub><sup>2-</sup>(aq)<br>
            The H<sup>+</sup> ions in the solution are attracted towards the zinc strip to capture the
            electrons on it. Hydrogen ions, after receiving the electrons become hydrogen gas (H<sub>2</sub>). Using
            chemical symbols, this can be written as follows.<br>
            <br>
            2H+(aq) + 2e&rarr;H<sub>2</sub>(g)&#x21E2;&#x2461;<br>
            <br>
            The reactions written as &#x2460; and &#x2461; above, depicting the conversion of one chemical
            species into another, either by removing or accepting electrons, are called 'half reactions'.
            By adding two half reactions appropriately, the balanced ionic equation can be obtained.<br>
            <br>
            Zn(s)&rarr;Zn<sup>2+</sup>(aq) + 2e&#x21E2;&#x2460;<br>
            <br>
            2H<sup>+</sup>(aq) + 2e&rarr;H(g)&#x21E2;&#x2461;<br>
            <br>
            &#x2460; + &#x2461; &rArr; Zn(s) + 2H<sup>+</sup>(aq) +
            <del>2e</del>&rarr;Zn<sup>2+</sup>(aq) +
            <del>2e</del>
            + H<sub>2</sub>(g)
            <br>
            Zn(s) + 2H<sup>+</sup>(aq)&rarr;Zn<sup>2+</sup>(aq) + H<sub>2</sub>(g)<br>
            <br>
            Next, let us consider how this reaction can be represented by a balanced chemical equation.
            The hydrogen ions (H<sup>+</sup>) were added to the solution by the dissociation of sulphuric
            acid (H<sub>2</sub>SO<sub>4</sub>). When sulphuric acid dissociates sulphate ions
            (SO<sub>4</sub><sup>2-</sup>) are also added to the medium in addition to H+ ions. But sulphate
            ions do not undergo any change during the reaction. So, we add SO<sub>4</sub><sup>2-</sup> to
            both sides.

            Zn(s) + 2H<sup>+</sup>(aq) + SO<sub>4</sub><sup>2-</sup>(aq)&rarr;Zn<sup>2+</sup>(aq) + SO<sub>4</sub><sup>2-</sup>(aq)
            + H<sub>2</sub>(g)<br>
            <br>
            H2SO4 ZnSO4<br>
            <br>
            Zn(s)+ H<sub>2</sub>SO<sub>4</sub>(aq)&rarr;ZnSO<sub>4</sub>(aq) + H<sub>2</sub>(g)<br>
            <br>
            Given above is the complete reaction for which zinc metal reacts with dilute sulphuric acid. If
            the exchange of electrons taking place between the zinc metal and H<sup>+</sup> ions during the
            above process occurs through an external conductor, we can produce an electric current.
          </div>
          <br>
          <br>
          <div class="activity">
              Let us do the following activity to see whether this can be done.<br>
            <div class="images">
              <img src="../../assets/images/electro-chemical-cells/activity_12.1.2.png"
                   style="width:550px;height:300px;">
            </div>
            <br>
            In this, it can be observed that the Ammeter pointer is deflected, zinc strip is dissolved and
            gas bubbles are evolved at the copper strip. Let us explore the reasons for these observations.
            Here too, zinc atoms become zinc ions (Zn<sup>2+</sup>) leaving electrons on the metal. Therefore, the zinc
            strip dissolves.<br>
            <br>
            The electrons accumulated on the zinc strip, flow towards the copper strip through an external
            wire. This flow of electrons is considered an electric current. Deflection of the Ammeter shows
            that an electric current flows through the circuit. Hence in this set up, H<sup>+</sup> ions in the solution
            move toward the copper strip and receive electrons from it. Therefore, hydrogen gas bubbles are
            liberated at the copper strip.<br>
            Reaction at the zinc strip<br>
            Zn (s)&rarr;Zn<sup>2+</sup>(aq)+ 2e&#x21E2;&#x2460;
            <br>
            Reaction at the copper strip<br>
            2H<sup>+</sup>(aq)+ 2e&rarr;H<sub>2</sub>(g)&#x21E2;&#x2461;<br>
            <br>
            In the above reaction it was confirmed that an electron current flows from zinc to copper in the
            external wire. A current of electrons means an electric current. In this, a chemical reaction has
            generated an electric current. A set up of this kind used to generate electricity by a chemical
            reaction is known as an electrochemical cell. The conducting substances dipped in the electrolyte
            here are called electrodes.<br>
            <br>
            In the above cell, zinc strip and copper strip act as electrodes. The balanced ionic equation
            obtained by adding the half reactions &#x2460; and &#x2461; above is the electrochemical reaction
            taking place in the cell.<br>
            &#x2460; + &#x2461; &rArr; Zn (s) + 2H<sup>+</sup>(aq)&rarr;Zn<sup>2+</sup>(aq)+ H<sub>2</sub>(g)<br>
            <br>
            Let us further consider the reaction occurring at the zinc electrode in the above cell.
            <br>
            Zn (s)&rarr;Zn<sup>2+</sup>(aq)+ 2e&#x21E2;&#x2460;
            <br>
            Loss of electrons from a given species (atoms, molecules or ions) is referred to as oxidation.
            Therefore, what is happening at the zinc strip is <b>oxidation</b>. If oxidation occurs at a certain
            electrode, that electrode is defined as the <b>anode</b>. Accordingly, the zinc strip is the anode of
            the above cell. Equation 1 represents the <b>oxidation half reaction</b> taking place at the anode.
            Since zinc atoms dissolve into the solution leaving electrons on the zinc plate, the zinc plate
            gets negatively charged relative to the copper plate. Therefore, zinc electrode is the <b>negative
            terminal</b> of the cell.
            <br>
            Next let us consider the reaction occurring at the copper strip.
            <br>
            2H<sup>+</sup>(aq) + 2e&rarr;H2(g)&#x21E2;&#x2461;
            <br>
            The hydrogen ions (H<sup>+</sup>) gaining electrons turn into hydrogen gas molecules (H<sub>2</sub>).
            Gaining electrons by a given species (atoms, molecules, ions) is described as a <b>reduction</b>. Since
            gaining of electrons or a reduction occurs at the copper electrode, reaction &#x2461; is the <b>reduction
            half reaction</b>.<br>
            <br>
            If reduction occurs at a certain electrode, it is defined as the <b>cathode</b>. Therefore, copper strip
            is the cathode of the cell. Since electrons flow to the copper strip, it is positively charged
            relative to the zinc strip. Therefore, copper electrode is the positive terminal of the cell.<br>
            <br>
            The electrochemical reaction of the cell can be obtained by adding the reactions &#x2460; and &#x2461;.<br>
            At the zinc electrode/negative terminal:<br>
            Zn (s)&rarr;Zn2+(aq)+ 2e&#x21E2;&#x2460; Anodic reaction
            <br>
            At the copper electrode/positive terminal:<br>
            2H<sup>+</sup>(aq) + 2e&rarr;H2(g)&#x21E2;&#x2461; Cathodic reaction<br>
            &#x2460; + &#x2461; &rArr; Zn(s) + 2H<sup>+</sup>(aq)&rarr;Zn<sup>2+</sup>(aq) + H<sub>2</sub>(g) Overall
            cell reaction
            <br>
            The following comparisons would be important for you to identify the anode and cathode of a given
            electrochemical cell.<br>
            <ul>
              <li>The metal placed higher in the activity series acts as the anode and the metal placed lower in the
                activity series acts as the cathode.
              </li>
              <li>Oxidation occurs at the anode and reduction occurs at the cathode.</li>
              <li>Anode becomes the negative terminal of the cell while cathode becomes the positive terminal of the
                cell.
              </li>
            </ul>
          </div>
          <br>
          <div class="note">
              <img src="../../assets/images/electro-chemical-cells/Note-pg83.png" style="width:550px;height:300px;"><br>
          </div>
          <div class="reaction">
            Next, let us consider a cell constructed using iron and copper electrodes.<br>
            <div class="images">
              <img src="../../assets/images/electro-chemical-cells/figure_12.1.6_Fe_Cu_electrodes.png"
                   style="width:500px;height:300px;">
            </div>
            <br>
            In the activity series, iron lies above copper. Therefore, what is subjected to <b>oxidation</b> and acts as
            the <b>anode</b> is the more reactive metal, iron.
            <br>
            Fe(s)&rarr;Fe<sup>2+</sup>(aq)+ 2e&#x21E2;&#x2463;
            <br>
            Since iron atoms dissolve into the solution leaving electrons on the iron strip, it is negatively
            charged relative to copper. Thus, iron electrode is the <b>negative terminal</b> of the cell.
            <br>
            In this cell also, the following reduction half reaction occurs at the less reactive copper metal.
            Therefore, copper electrode acts as the cathode of this cell.
            <br>
            2H<sup>+</sup>(aq) + 2e&rarr;H<sub>2</sub>(g)&#x21E2;&#x2464;
            <br>
            Electrons flow to the copper electrode across the external wire. Therefore, copper electrode is the
            <b>positive terminal</b> of the cell.<br>
            The overall ionic reaction of the cell can be obtained by adding the two half reactions &#x2463; and
            &#x2464;.
            <br>
            Fe(s) + 2H<sup>+</sup>(aq)&rarr;Fe<sup>2+</sup>(aq) + H<sub>2</sub>(g)
            <br>
            When a current is drawn from this cell it can be observed that the iron electrode dissolves and gas
            bubbles evolve at the copper electrode.
          </div>
          <br>
          <br>
          <div class="reaction">
            <p>
              Consider the following cell constructed using zinc and iron electrodes.
              <br>
            <div class="images">
              <img src="../../assets/images/electro-chemical-cells/figure_12.1.7_Zn_Fe_electrodes.png"
                   style="width:500px;height:300px;">
            </div>
            <br>
            In the activity series, zinc metal is placed above iron. Therefore, zinc which is the more reactive
            metal, undergoes oxidation and acts as the anode.
            <br>
            Reaction at the zinc electrode/anode.
            <br>
            Zn(s)&rarr;Zn<sup>2+</sup>(aq) + 2e&#x21E2;&#x2465;
            <br>
            Here too, as the zinc atoms dissolve into the solution leaving electrons on the zinc electrode, zinc
            becomes negatively charged relative to iron. For this reason, zinc electrode becomes the negative
            terminal of the cell.<br>
            <br>
            Reaction at the iron electrode/cathode.
            <br>
            2H<sup>+</sup>(aq) + 2e&rarr;H2(g)&#x21E2;&#x2466;
            <br>
            Because reduction occurs at iron, it acts as the cathode.
            <br>
            Electrons flow towards the iron electrode along the connecting wire. Hence iron electrode is the
            positive terminal of the cell.
            <br>
            The overall ionic reaction of the cell can be obtained by adding the reactions &#x2465; and &#x2466;.
            <br>
            Zn(s) + 2H<sup>+</sup>(aq)&rarr;Zn<sup>2+</sup>(aq) + H2(g)
            <br>
            When this cell operates, we will be able to see that the zinc electrode dissolves and gas bubbles
            evolve at the iron electrode.
            </p>
          </div>
        </div>
      </article>
    </section>
  `,
  styles: [
  ]
})
export class ChaptersChemComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
