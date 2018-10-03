INSERT INTO country (name) VALUES ('Germany');
INSERT INTO country (name) VALUES ('United Kingdom');
INSERT INTO country (name) VALUES ('Tunisia');
INSERT INTO country (name) VALUES ('France');
INSERT INTO network (alias, country_fk) VALUES ('TUNOR', 3);
INSERT INTO network (alias, country_fk) VALUES ('FRAF1',4);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('DEUD1', 1, 1);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('DEUD1', 1, 2);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('DEUD2', 1, 1);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('DEUD2', 1, 2);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('DEUE1', 1, 1);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('DEUE1', 1, 2);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('GBRVF', 1, 1);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('GBRVF', 1, 2);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('GBROR', 1, 1);
INSERT INTO coverage (alias, cov, network_fk) VALUES ('GBROR', 1, 2);

