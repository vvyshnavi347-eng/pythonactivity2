

### 1. Problem Statement

To develop a Python program that processes marks obtained by a student in multiple subjects, checks subject-wise pass criteria, applies the specified grace-mark policy, and generates the final result and classification without exceeding the maximum marks.

### 2. Algorithm

1. Start the program.
2. Read the number of subjects.
3. Enter the maximum marks and passing marks for each subject.
4. Enter the student's marks in each subject.
5. Calculate the grace marks required for subjects in which the student has failed.
6. Check whether the grace marks are within the permitted limit.
7. Add grace marks to eligible subjects.
8. Ensure that the final marks do not exceed the maximum marks.
9. Check the pass or fail status of each subject.
10. Calculate the total marks and percentage.
11. Display the final result.
12. Assign the classification based on the percentage:
    - 75% and above – Distinction
    - 60% to 74% – First Class
    - 50% to 59% – Second Class
    - Below 50% – Third Class
13. Stop the program.
### 5. Flowchart 



\#chatgpt-mermaid-\_r_e3\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_e3\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_e3\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_e3\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_e3\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_e3\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_e3\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_e3\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_e3\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_e3\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e3\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e3\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_e3\_ p{margin:0;}#chatgpt-mermaid-\_r_e3\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_e3\_ .label text,#chatgpt-mermaid-\_r_e3\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ .node rect,#chatgpt-mermaid-\_r_e3\_ .node circle,#chatgpt-mermaid-\_r_e3\_ .node ellipse,#chatgpt-mermaid-\_r_e3\_ .node polygon,#chatgpt-mermaid-\_r_e3\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ .rough-node .label text,#chatgpt-mermaid-\_r_e3\_ .node .label text,#chatgpt-mermaid-\_r_e3\_ .image-shape .label,#chatgpt-mermaid-\_r_e3\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_e3\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ .rough-node .label,#chatgpt-mermaid-\_r_e3\_ .node .label,#chatgpt-mermaid-\_r_e3\_ .image-shape .label,#chatgpt-mermaid-\_r_e3\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_e3\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_e3\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e3\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e3\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_e3\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_e3\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_e3\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_e3\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_e3\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_e3\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e3\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_e3\_ .icon-shape,#chatgpt-mermaid-\_r_e3\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_e3\_ .icon-shape p,#chatgpt-mermaid-\_r_e3\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_e3\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_e3\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_e3\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_e3\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_e3\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_e3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_e3\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_e3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_e3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e3\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_e3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e3\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_e3\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_e3\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_e3\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_e3\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ .node rect,#chatgpt-mermaid-\_r_e3\_ .node circle,#chatgpt-mermaid-\_r_e3\_ .node ellipse,#chatgpt-mermaid-\_r_e3\_ .node polygon,#chatgpt-mermaid-\_r_e3\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_e3\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_e3\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_e3\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_e3\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e3\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of subjectsEnter maximum marks, passingmarks and grace limitEnter marks for each subjectCalculate marks required topassIs student failed in subject?Keep original marksRequired grace marks withinlimit?Add grace marksKeep original marksCheck maximum marks limitCalculate total and percentageAll subjects passed?Final 

### 3. Sample Input

```
Enter number of subjects: 5

Enter maximum marks: 100
Enter passing marks: 35
Enter grace mark limit: 5

Enter marks for Subject 1: 85
Enter marks for Subject 2: 72
Enter marks for Subject 3: 32
Enter marks for Subject 4: 90
Enter marks for Subject 5: 68
```

### 4. Sample Output

```

Subject 1: 85
Subject 2: 72
Subject 3: 35 (Grace Marks: 3)
Subject 4: 90
Subject 5: 68

Total Marks: 350 / 500
Percentage: 70%

Subject Status: PASS
Final Result: PASS
Classification: FIRST CLASS
```

