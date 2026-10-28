import csv, collections, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
here=os.path.dirname(os.path.abspath(__file__)); logs=os.path.dirname(here)
rows=list(csv.DictReader(open(os.path.join(logs,"defect_log.csv"))))
sev=["Critical","High","Medium","Low"]
cats=sorted({r["Category"] for r in rows})
cnt=collections.Counter((r["Category"],r["Severity"]) for r in rows)
out=["# Summary: defects by category and severity\n","| Category | "+" | ".join(sev)+" | Total |","|---|"+"---|"*(len(sev)+1)]
for c in cats:
    v=[cnt[(c,s)] for s in sev]; out.append(f"| {c} | "+" | ".join(map(str,v))+f" | {sum(v)} |")
tot=[sum(cnt[(c,s)] for c in cats) for s in sev]
out.append("| **Total** | "+" | ".join(f"**{t}**" for t in tot)+f" | **{sum(tot)}** |")
open(os.path.join(logs,"summary.md"),"w").write("\n".join(out)+"\n")
fig,ax=plt.subplots(figsize=(9,5)); bottom=[0]*len(cats)
col={"Critical":"#8b1a1a","High":"#d9534f","Medium":"#f0ad4e","Low":"#5bc0de"}
for s in sev:
    h=[cnt[(c,s)] for c in cats]; ax.barh(cats,h,left=bottom,label=s,color=col[s]); bottom=[b+x for b,x in zip(bottom,h)]
ax.set_xlabel("Number of defects"); ax.set_title("PSVS-REQ-v1.0 defects by category and severity"); ax.legend(); ax.invert_yaxis()
plt.tight_layout(); plt.savefig(os.path.join(logs,"defects_by_category.png"),dpi=150)
