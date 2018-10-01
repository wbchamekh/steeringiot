INSERT INTO country (name) VALUES ('Germany');
INSERT INTO country (name) VALUES ('United Kingdom');
INSERT INTO network (alias) VALUES ('TUNOR');
INSERT INTO network (alias) VALUES ('FRAF1');
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('DEUD1', 1, 1, 1);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('DEUD1', 1, 2, 1);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('DEUD2', 1, 1, 1);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('DEUD2', 1, 2, 1);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('DEUE1', 1, 1, 1);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('DEUE1', 1, 2, 1);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('GBRVF', 1, 1, 2);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('GBRVF', 1, 2, 2);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('GBROR', 1, 1, 2);
INSERT INTO coverage (alias, cov, network_fk, country_fk) VALUES ('GBROR', 1, 2, 2);

