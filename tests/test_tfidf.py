from src.tfidf import TfidfExtractor


documents = [
    """
    Operating systems manage processes and memory.
    Processes require memory to execute.
    """,

    """
    Computer networks use packets.
    Networks use routers to forward packets.
    """,

    """
    Operating systems schedule processes.
    Process scheduling determines which process runs.
    """
]


extractor = TfidfExtractor(max_features=10)

concepts = extractor.extract(documents)


print("\nTop concepts:\n")

for concept, score in concepts:

    print(
        f"{concept:20} {score:.3f}"
    )