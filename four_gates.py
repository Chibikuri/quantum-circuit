from qiskit import QuantumProgram
#from qiskit.tools.visualization import plot_histogram
#from qasm2image import qasm2png

class Quantum_culc:
    qp = QuantumProgram()
    qr = qp.create_quantum_register("qr", 3)
    cr = qp.create_classical_register("cr", 3)

    @classmethod
    def A_circuit(self):
        qp = self.qp
        qr = self.qr
        cr = self.cr
        qc = self.qp.create_circuit("A_circuit", [qr], [cr])
        qc.cx(qr[0], qr[2])
        qc.measure(qr[0], cr[0])
        qc.measure(qr[1], cr[1])
        qc.measure(qr[2], cr[2])
        result_A = qp.execute("A_circuit")
        print(result_A.get_counts("A_circuit"))
        #print(qc.qasm())
        #print(qasm2png(qc.qasm()))

    @classmethod
    def B_circuit(self):
        qp = self.qp
        qr = self.qr
        cr = self.cr
        qc = self.qp.create_circuit("B_circuit", [qr], [cr])
        qc.cx(qr[1], qr[0])
        qc.cx(qr[0], qr[1])
        qc.cx(qr[1], qr[2])
        qc.cx(qr[0], qr[1])
        qc.cx(qr[1], qr[0])
        qc.measure(qr[0], cr[0])
        qc.measure(qr[1], cr[1])
        qc.measure(qr[2], cr[2])
        result_B = qp.execute("B_circuit")
        print(result_B.get_counts("B_circuit"))


    @classmethod
    def C_circuit(self):
        qp = self.qp
        qr = self.qr
        cr = self.cr
        qc = self.qp.create_circuit("C_circuit", [qr], [cr])
        qc.cx(qr[0], qr[1])
        qc.cx(qr[1], qr[2])
        qc.cx(qr[0], qr[1])
        qc.cx(qr[1], qr[2])
        qc.measure(qr[0], cr[0])
        qc.measure(qr[1], cr[1])
        qc.measure(qr[2], cr[2])
        result_C = qp.execute("C_circuit")
        print(result_C.get_counts("C_circuit"))

    @classmethod
    def D_circuit(self):
        qp = self.qp
        qr = self.qr
        cr = self.cr
        qc = self.qp.create_circuit("D_circuit", [qr], [cr])
        qc.h(qr[0])
        qc.h(qr[2])
        qc.cx(qr[1], qr[2])
        qc.cx(qr[2], qr[1])
        qc.cx(qr[2], qr[1])
        qc.cx(qr[1], qr[2])
        qc.h(qr[0])
        qc.h(qr[2])
        qc.measure(qr[0], cr[0])
        qc.measure(qr[1], cr[1])
        qc.measure(qr[2], cr[2])
        result_D = qp.execute("D_circuit")
        print(result_D.get_counts("D_circuit"))


if __name__ == '__main__':
        Quantum_culc.A_circuit()
        Quantum_culc.B_circuit()
        Quantum_culc.C_circuit()
        Quantum_culc.D_circuit()
