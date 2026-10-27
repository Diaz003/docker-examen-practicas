--
-- PostgreSQL database dump
--

\restrict V2KYdzUfDqXF00qhXx4C7esmcC1FxT2cMfbUbtpE3Qcpb7ZpeYjR7XC7F8VkVRJ

-- Dumped from database version 15.19
-- Dumped by pg_dump version 15.19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: sales; Type: TABLE; Schema: public; Owner: usuario9
--

CREATE TABLE public.sales (
    id integer NOT NULL,
    articulo character varying(100) NOT NULL,
    cantidad integer NOT NULL,
    vendedor character varying(100) NOT NULL
);


ALTER TABLE public.sales OWNER TO usuario9;

--
-- Name: sales_id_seq; Type: SEQUENCE; Schema: public; Owner: usuario9
--

CREATE SEQUENCE public.sales_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sales_id_seq OWNER TO usuario9;

--
-- Name: sales_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usuario9
--

ALTER SEQUENCE public.sales_id_seq OWNED BY public.sales.id;


--
-- Name: sales id; Type: DEFAULT; Schema: public; Owner: usuario9
--

ALTER TABLE ONLY public.sales ALTER COLUMN id SET DEFAULT nextval('public.sales_id_seq'::regclass);


--
-- Data for Name: sales; Type: TABLE DATA; Schema: public; Owner: usuario9
--

COPY public.sales (id, articulo, cantidad, vendedor) FROM stdin;
1	Teclado Mecánico RGB	3	Alfonso Díaz Morales
2	Monitor Gaming	10	Alfonso Díaz Morales
\.


--
-- Name: sales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usuario9
--

SELECT pg_catalog.setval('public.sales_id_seq', 2, true);


--
-- Name: sales sales_pkey; Type: CONSTRAINT; Schema: public; Owner: usuario9
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict V2KYdzUfDqXF00qhXx4C7esmcC1FxT2cMfbUbtpE3Qcpb7ZpeYjR7XC7F8VkVRJ

