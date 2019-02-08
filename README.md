# Reiknirit Verkefni 3

* ### [Dæmi 1](https://github.com/MattiMatt8/Reiknirit_v3/blob/master/d%C3%A6mi1.pdf)
* ### Dæmi 2
    * #### O(2^n) þar sem hvert skipti þar sem n hækkar þá tvöfaldast fjöldi kalla í sig sjálft en jafnan til að finna fjöldi kalla er (2^n) - 1 þar sem það byrjar á 1 og er alltaf oddatala eins og næsta er 3 og síðan 7.
* ### Dæmi 3
    * #### O(n)
        * #### Það er reiknirit sem keyrir jafnt oft og n eins og einfalt reiknirit sem er að leita í lista og er með eina lykkju sem fer í gegnum hvert tag fyrir sig í listanum og í versta falli tekur n langann tíma að keyra.
    * #### O(n^2)
        * #### Það er reiknirit sem tekur n^2 tíma að keyra og er eins og tvær lykkjur þar sem önnur er inn í hinni eins og selection sort reiknirit fyrir tölu lista þar sem fyrsta loopið myndi fara í gegnum hverja tölu fyrir sig og síðan seinni kíkir hvort hvert stak sé minna en öll stök á eftir því annars skiptir þeim um stað og fer í næstu tölu.
    * #### O(log(n))
        * #### Það er reiknirit sem tekur log(n) tíma að keyra og væri reiknirit sem myndi ekki þurfa að fara í gegnum allar tölur eins og tvíundarleit þar sem það byrjar að skipta til dæmis lista af tölum í tvennt og ber tölununa í miðjum listanum við það sem er leitað af og ef það er hærra þá heldur það áfram með helminginn með hærri tölunum í, annars myndi það halda áfram með hinn helminginn og síðan heldur það áfram að deila í tvennt, bera saman og alveg þangað til talan er fundið.
* ### Dæmi 4
    * #### a ) 26 nCr x
        * #### Þar sem x er fjöldi bókstafa hvert orða á að hafa.
    * #### b ) Flækjutími fallsins er O(nCr)
        * #### Tímamælingar
            * n = 2 tekur sirka 0,09 ms
            * n = 3 tekur sirka 0,8 ms
            * n = 4 tekur sirka 5,4 ms
            * Hver hækkun á n hækkar keyrslu tímann margfalt oftar.
* ### Dæmi 5
    * #### a )
        * Já, það getur munað vel miklu miðað við hversu mikill munur er á lengdum strengjann til dæmis:
            * Listi með 396 strengi af lengdinni 1 tekur rúmlega 0,6 ms að keyra
            * Listi með 396 strengi af lengdinni 10 tekur rúmlega 1,6 ms að keyra
    * #### b )
        * #### Tímamælingar
            * n = 2 tekur sirka 0,17 ms
            * n = 3 tekur sirka 32 ms
            * n = 4 tekur sirka 82000 ms
            * Þetta sýnir hversu hægt bubblesort verður fljótt þegar listarnir til að larna verða stærri og stærri.
        * #### Flækjutími bubble sort er: O(n^2)
    * #### c )
        * Ég prufaði að tímamæla lista með heiltölum og strengjum og fékk þetta út
            * Listi með 396 heiltölur sem eru frá 1-9 tekur rúmlega 0,6 ms að keyra
            * Listi með 396 heiltölur sem eru frá 1.000.000.000 - 9.999.999.999 tekur rúmlega 1,1 ms að keyra
            * Ef maður ber þetta saman við niðurstöðurnar úr A liðnum þá er það hraðara að raða heiltölum en það eru samt tilvik þar sem það tekur svipaðann tíma eða sama miðað við hversu stórar tölur er verið að vinna með og hversu langir strengirnir sem er verið að vinna með eins og að raða tölum frá 1-9 og að raða strengjum af lengindinni 1.