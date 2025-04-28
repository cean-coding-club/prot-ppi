# 📄 Summary: Proteins and FASTA Sequences

## 🧬 What is a Protein?

- A **protein** is a large biomolecule made of **amino acids**.
- Proteins have multiple levels of structure:
  - **Primary structure**: Amino acid sequence
  - **Secondary structure**: Alpha-helices, beta-sheets
  - **Tertiary structure**: 3D folded shape
  - **Quaternary structure**: Complexes of multiple protein units
- Proteins perform essential biological functions (enzymes, signaling, defense, structure).

---

## 📚 What is a FASTA Sequence?

- **FASTA format** is a simple text-based standard for representing sequences.
- Structure:
  1. **Header line** (starts with `>`) containing the sequence name or description.
  2. **Sequence lines** made up of single-letter amino acid codes.

### Example:

```plaintext
>Protein_X
MKTFFISLLFLFSSAYSRGVFRRDTHKSEIAHRFKDLGE
```

# 🧠 Relevance of Protein Sequences for PPI Analysis

**Protein-Protein Interactions (PPIs)** are driven largely by the **physicochemical properties** of the interacting protein surfaces.

Even without knowing the full 3D structure, the **primary amino acid sequence** can reveal important information about a protein's interaction potential.

By analyzing sequences from FASTA files, we can:

- Predict regions likely to interact.
- Identify features such as disorder, charge, hydrophobicity, and domain presence.
- Pre-screen proteins for interaction likelihood before running heavy computational or experimental assays.

---

## 📌 Key Properties Relevant for PPI Screening

| Property             | Importance for PPI                                                             |
|:---------------------|:--------------------------------------------------------------------------------|
| **Length**            | Very short or very long proteins may behave differently in interaction dynamics. |
| **Charge**            | Electrostatic complementarity drives binding (positive vs negative patches).    |
| **Hydrophobicity**    | Hydrophobic patches often form stable interaction surfaces.                     |
| **Disorder Regions**  | Flexible, disordered regions can mediate transient and flexible interactions.    |
| **Surface Accessibility** | Surface-exposed residues are more likely to participate in PPIs.           |
| **Domain/Motif Content** | Specific domains or motifs (e.g., SH3, PDZ, LRR) can predict known binding behaviors. |

---

## ✅ Quick Table

| Term               | Description                                         |
|:-------------------|:----------------------------------------------------|
| **Protein**         | Chain of amino acids performing biological functions |
| **FASTA**           | Text format for sequence storage and analysis       |
| **Header**          | `>` followed by protein ID or description           |
| **Sequence**        | Single-letter amino acid codes                      |
| **Primary Structure** | Linear sequence; starting point for computational predictions |
