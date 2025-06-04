!(register-module! ../new_MeTTa_project)
!(import! &self llm_summary)
!(import! &self new_MeTTa_project:nodes)

(= (h )(match &self 
       (gene_type (gene $gen) $type) 
       (match &self (chr (gene $gen) $chr) 
       (match &self (start (gene $gen) $start) 
       (match &self (end (gene $gen) $end)
       (match &self (gene_name (gene $gen) $name) 
       (match &self (synonyms (gene $gen) $synonyms) 
       ((gene_summarizer $gen (gene $gen $type $chr $start $end $name $synonyms))))))))
  ))

!(h)