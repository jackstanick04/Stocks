-- table to hold the companies themselves
-- need to only create if it doesnt exist or it will try and make new table every time file is ran
DROP TABLE IF EXISTS companies;
CREATE TABLE IF NOT EXISTS companies (
    -- data for each company
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    ticker TEXT,
    industry TEXT,
    current_price REAL,
    market_cap TEXT
);

-- company-specific data insertions (one row per company) bulk insert
INSERT INTO companies (id, name, ticker, industry, current_price, market_cap) VALUES
(1, 'Amazon', 'AMZN', 'Technology', 237.68, '2.50T'),
(2, 'Apple', 'AAPL', 'Technology', 236.00, '3.55T'),
(3, 'Coca-Cola', 'KO', 'Consumer', 63.48, '273.46B'),
(4, 'Costco', 'COST', 'Consumer', 979.88, '434.97B'),
(5, 'JP Morgan', 'JPM', 'Finance', 267.30, '752.54B'),
(6, 'Microsoft', 'MSFT', 'Technology', 415.06, '3.09T'),
(7, 'Nike', 'NKE', 'Sport', 76.90, '113.74B'),
(8, 'Oracle', 'ORCL', 'Technology', 170.06, '475.65B'),
(9, 'Pfizer', 'PFE', 'Health', 26.52, '150.29B'),
(10, 'Tesla', 'TSLA', 'Technology', 404.60, '1.27T');

-- table to hold each invididual stock based on company and year, again only created if it does not exist
DROP TABLE IF EXISTS shares;
CREATE TABLE IF NOT EXISTS shares (
    -- data for each share
    share_id INTEGER PRIMARY KEY,
    year INTEGER,
    company_id INTEGER,
    price REAL
);

-- bulk insert statement for each company separately (for organization)
-- real data from past ten years prices, and then the current price as of 2/2/2025

-- amazon
INSERT INTO shares (share_id, year, company_id, price) VALUES
(1, 2015, 1, 23.85),
(2, 2016, 1, 34.89),
(3, 2017, 1, 48.29),
(4, 2018, 1, 81.89),
(5, 2019, 1, 89.24),
(6, 2020, 1, 133.72),
(7, 2021, 1, 166.79),
(8, 2022, 1, 125.80),
(9, 2023, 1, 121.37),
(10, 2024, 1, 184.63);

-- apple
INSERT INTO shares (share_id, year, company_id, price) VALUES
(11, 2015, 2, 26.96),
(12, 2016, 2, 23.98),
(13, 2017, 2, 35.17),
(14, 2018, 2, 44.84),
(15, 2019, 2, 50.18),
(16, 2020, 2, 92.94),
(17, 2021, 2, 138.35),
(18, 2022, 2, 152.78),
(19, 2023, 2, 171.29),
(20, 2024, 2, 206.77);

-- cocacola
INSERT INTO shares (share_id, year, company_id, price) VALUES
(21, 2015, 3, 30.46),
(22, 2016, 3, 33.19),
(23, 2017, 3, 34.96),
(24, 2018, 3, 37.01),
(25, 2019, 3, 42.83),
(26, 2020, 3, 43.44),
(27, 2021, 3, 48.60),
(28, 2022, 3, 57.11),
(29, 2023, 3, 57.08),
(30, 2024, 3, 62.96);

-- costco
INSERT INTO shares (share_id, year, company_id, price) VALUES
(31, 2015, 4, 124.19),
(32, 2016, 4, 131.46),
(33, 2017, 4, 148.02),
(34, 2018, 4, 189.27),
(35, 2019, 4, 240.12),
(36, 2020, 4, 305.42),
(37, 2021, 4, 401.99),
(38, 2022, 4, 490.84),
(39, 2023, 4, 519.15),
(40, 2024, 4, 822.03);

-- jp morgan
INSERT INTO shares (share_id, year, company_id, price) VALUES
(41, 2015, 5, 49.24),
(42, 2016, 5, 52.11),
(43, 2017, 5, 74.87),
(44, 2018, 5, 92.03),
(45, 2019, 5, 97.41),
(46, 2020, 5, 94.14),
(47, 2021, 5, 141.83),
(48, 2022, 5, 119.88),
(49, 2023, 5, 139.22),
(50, 2024, 5, 203.50);

-- microsoft
INSERT INTO shares (share_id, year, company_id, price) VALUES
(51, 2015, 6, 40.82),
(52, 2016, 6, 49.62),
(53, 2017, 6, 66.26),
(54, 2018, 6, 94.78),
(55, 2019, 6, 124.13),
(56, 2020, 6, 185.66),
(57, 2021, 6, 267.98),
(58, 2022, 6, 263.23),
(59, 2023, 6, 310.43),
(60, 2024, 6, 418.75);

-- nike
INSERT INTO shares (share_id, year, company_id, price) VALUES
(61, 2015, 7, 49.62),
(62, 2016, 7, 51.14),
(63, 2017, 7, 51.31),
(64, 2018, 7, 68.03),
(65, 2019, 7, 81.77),
(66, 2020, 7, 101.44),
(67, 2021, 7, 144.67),
(68, 2022, 7, 112.94),
(69, 2023, 7, 110.22),
(70, 2024, 7, 86.98);

-- oracle
INSERT INTO shares (share_id, year, company_id, price) VALUES
(71, 2015, 8, 35.37),
(72, 2016, 8, 34.55),
(73, 2017, 8, 41.62),
(74, 2018, 8, 43.61),
(75, 2019, 8, 49.56),
(76, 2020, 8, 51.74),
(77, 2021, 8, 77.58),
(78, 2022, 8, 73.25),
(79, 2023, 8, 102.25),
(80, 2024, 8, 140.14);

-- pfizer
INSERT INTO shares (share_id, year, company_id, price) VALUES
(81, 2015, 9, 21.91),
(82, 2016, 9, 22.11),
(83, 2017, 9, 23.84),
(84, 2018, 9, 28.44),
(85, 2019, 9, 30.00),
(86, 2020, 9, 28.80),
(87, 2021, 9, 36.24),
(88, 2022, 9, 44.22),
(89, 2023, 9, 33.94),
(90, 2024, 9, 27.15);

-- tesla
INSERT INTO shares (share_id, year, company_id, price) VALUES
(91, 2015, 10, 15.34),
(92, 2016, 10, 13.98),
(93, 2017, 10, 20.95),
(94, 2018, 10, 21.15),
(95, 2019, 10, 18.24),
(96, 2020, 10, 96.67),
(97, 2021, 10, 260.00),
(98, 2022, 10, 263.09),
(99, 2023, 10, 217.48),
(100, 2024, 10, 230.62);
