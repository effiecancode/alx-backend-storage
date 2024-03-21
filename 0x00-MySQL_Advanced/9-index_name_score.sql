-- Script that creates an index indx_name_first_score on
-- the tabl names and the first letter of name and the score
CREATE INDEX idx_name_first_score on names(name(1), score)
