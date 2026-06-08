param(
    [string]$Repo = "asmatkhan925/AIR_review"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI is not installed. Install it, run 'gh auth login', then rerun this script."
}

gh auth status | Out-Host

$labels = @(
    @{ Name = "literature-search"; Color = "1d76db"; Description = "Search, screening, and literature coverage tasks" },
    @{ Name = "paper-note"; Color = "5319e7"; Description = "Structured notes for individual papers" },
    @{ Name = "matrix-update"; Color = "0e8a16"; Description = "Updates to synthesis, evidence, dataset, or model matrices" },
    @{ Name = "drafting"; Color = "fbca04"; Description = "Manuscript drafting and section revision" },
    @{ Name = "citation-check"; Color = "d93f0b"; Description = "Citation verification and reference reliability" },
    @{ Name = "figure"; Color = "c5def5"; Description = "Figure planning, design, or revision" },
    @{ Name = "table"; Color = "bfdadc"; Description = "Table planning, design, or revision" },
    @{ Name = "quality-control"; Color = "b60205"; Description = "Review quality gates and reviewer-risk controls" },
    @{ Name = "needs-verification"; Color = "e99695"; Description = "Requires source, citation, or evidence verification" },
    @{ Name = "high-priority"; Color = "ff0000"; Description = "High-priority project task" }
)

foreach ($label in $labels) {
    gh label create $label.Name `
        --repo $Repo `
        --color $label.Color `
        --description $label.Description `
        --force
}

$issues = @(
    @{
        Title = "Fill foundation model matrix for Whisper, MMS, XLS-R, OMNIASR"
        Labels = "matrix-update,needs-verification,high-priority"
        Body = "Populate and verify the foundation model matrix entries for Whisper, MMS, XLS-R, OMNIASR, and related newer speech-language models. Confirm year, training type, language coverage, data scale, ASR capability, adaptation options, and known low-resource limitations."
    },
    @{
        Title = "Screen 30 papers on pseudo-labeling and KD for low-resource ASR"
        Labels = "literature-search,paper-note,high-priority"
        Body = "Screen at least 30 papers on self-training, pseudo-labeling, sequence-level KD, multi-teacher KD, confidence filtering, and teacher disagreement in low-resource ASR. Log searches and create full notes for the strongest papers."
    },
    @{
        Title = "Draft Section 8 on pseudo-labeling and knowledge distillation"
        Labels = "drafting,high-priority"
        Body = "Draft the pseudo-labeling and KD section as critical synthesis, not a paper list. Connect the section to the evidence-to-claim matrix and adaptation strategy matrix."
    },
    @{
        Title = "Verify all references used in introduction"
        Labels = "citation-check,needs-verification,high-priority"
        Body = "Verify title, year, venue, DOI or URL, citation key, and main use for every reference used in the introduction. Update 03_references/citation_verification_log.csv before manuscript use."
    },
    @{
        Title = "Build taxonomy figure for foundation-model-era low-resource ASR"
        Labels = "figure,quality-control"
        Body = "Design a taxonomy figure that organizes low-resource ASR by resources, model families, adaptation methods, pseudo-labeling/KD, evaluation, and multimodal or LLM-assisted future directions."
    }
)

foreach ($issue in $issues) {
    gh issue create `
        --repo $Repo `
        --title $issue.Title `
        --body $issue.Body `
        --label $issue.Labels
}

Write-Host "GitHub labels and seed issues created for $Repo."

