"""
Challenge 3.4 Solver
Goal 1: Find Bob's next OTP given f25a, cbc9.
Goal 2: Find Charlotte's potential next OTP (OTP3) given 1ccf, 1*** and n < 100.

Use tiny_h_otp.py to compute TinyH-OTP values.

"""

import time
import tiny_h_otp

# Constants
MAX_16BIT = 0x10000  # 65536
MAX_STEP = 100
MAX_OTP_ATTEMPTS = 3

class OTPSolver:
    """Solver for TinyH-OTP challenges."""
    
    def __init__(self):
        self.start_time = time.time()
    
    def _get_elapsed_time(self) -> float:
        """Get elapsed time since solver start."""
        return time.time() - self.start_time
    
    def find_bob_solution(self, otp1: str, otp2: str) -> tuple[str, int, str] | None:
        """
        Find Bob's Master Password and compute next OTP.
        Returns (master_password, step, next_otp) or None if not found.
        """
        otp1_int = int(otp1, 16)
        otp2_int = int(otp2, 16)
        
        print("Searching for Bob's master password...")
        
        # Try all possible master passwords
        for mp_int in range(MAX_16BIT):
            mp_hex = f"{mp_int:04x}"
            state = mp_hex
            
            # Try all possible steps (n < 100)
            for n in range(MAX_STEP):
                current_state_int = int(state, 16)
                
                # Check if this state produces OTP1
                if (current_state_int ^ mp_int) == otp1_int:
                    # Get next state and check OTP2
                    next_state = tiny_h_otp.TinyH(state)
                    next_state_int = int(next_state, 16)
                    
                    if (next_state_int ^ mp_int) == otp2_int:
                        # Found match! Compute OTP3
                        state_after = tiny_h_otp.TinyH(next_state)
                        otp3_int = int(state_after, 16) ^ mp_int
                        otp3_hex = f"{otp3_int:04x}"
                        
                        print(f"Found Bob's Master Password: {mp_hex}, at step n={n}")
                        print(f"Bob's next OTP is: {otp3_hex}")
                        return mp_hex, n, otp3_hex
                
                # Move to next state
                state = tiny_h_otp.TinyH(state)
        
        return None
    
    def find_charlotte_solutions(self, otp1: str, otp2_prefix: str) -> list:
        """
        Find all possible solutions for Charlotte's OTP.
        Returns list of (mp, step, otp2, otp3) tuples.
        """
        otp1_int = int(otp1, 16)
        solutions = []
        
        print("\nSearching for Charlotte's solutions...")
        
        # Try all possible master passwords
        for mp_int in range(MAX_16BIT):
            mp_hex = f"{mp_int:04x}"
            state = mp_hex
            
            # Initialize state through n iterations
            for n in range(MAX_STEP):
                state = tiny_h_otp.TinyH(state)
                current_state_int = int(state, 16)
                
                # Check if current state produces OTP1
                if (current_state_int ^ mp_int) == otp1_int:
                    # Compute OTP2
                    next_state = tiny_h_otp.TinyH(state)
                    otp2_int = int(next_state, 16) ^ mp_int
                    otp2_hex = f"{otp2_int:04x}"
                    
                    # Check if OTP2 matches prefix
                    if otp2_hex.startswith(otp2_prefix):
                        # Compute OTP3
                        state_after = tiny_h_otp.TinyH(next_state)
                        otp3_int = int(state_after, 16) ^ mp_int
                        otp3_hex = f"{otp3_int:04x}"
                        
                        solutions.append((mp_hex, n + 1, otp2_hex, otp3_hex))
        
        return solutions
    
    def analyze_solutions(self, solutions: list) -> set[str]:
        """Analyze and display results for Charlotte's OTP."""
        if not solutions:
            print("No solutions found for Charlotte.")
            return set()
        
        # Extract unique OTP3 values
        unique_otp3s = {sol[3] for sol in solutions}
        
        print(f"\nFound {len(solutions)} possible solutions for Charlotte.")
        print(f"Found {len(unique_otp3s)} unique OTP3 candidates.\n")
        
        # Display unique OTP3 candidates
        print("Charlotte's OTP3 candidates (unique):")
        for otp3 in sorted(unique_otp3s):
            print(f"  {otp3}")
        
        # Calculate probabilities
        prob_per_candidate = 1 / len(unique_otp3s)
        success_prob = min(MAX_OTP_ATTEMPTS, len(unique_otp3s)) / len(unique_otp3s)
        
        print(f"\nEach candidate probability: 1/{len(unique_otp3s)} = {prob_per_candidate:.0%}")
        print(f"\nWith {MAX_OTP_ATTEMPTS} attempts and {len(unique_otp3s)} candidates:")
        print(f"Success probability: {MAX_OTP_ATTEMPTS}/{len(unique_otp3s)} = {success_prob:.0%}")
        
        return unique_otp3s
    
    def solve_bob_challenge(self) -> None:
        """Solve Bob's OTP challenge."""
        BOB_OTP1 = "f25a"
        BOB_OTP2 = "cbc9"
        
        result = self.find_bob_solution(BOB_OTP1, BOB_OTP2)
        if result is None:
            print("ERROR: Could not find solution for Bob's OTPs")
    
    def solve_charlotte_challenge(self) -> None:
        """Solve Charlotte's OTP challenge."""
        CHARLOTTE_OTP1 = "1ccf"
        CHARLOTTE_OTP2_PREFIX = "1"
        
        solutions = self.find_charlotte_solutions(CHARLOTTE_OTP1, CHARLOTTE_OTP2_PREFIX)
        self.analyze_solutions(solutions)
    
    def run_all_challenges(self) -> None:
        """Run both challenges."""
        print("=" * 50)
        print("TinyH-OTP Challenge Solver")
        print("=" * 50)
        
        # Solve Bob's challenge
        print("\n" + "=" * 20 + " BOB'S CHALLENGE " + "=" * 20)
        self.solve_bob_challenge()
        
        # Solve Charlotte's challenge
        print("\n" + "=" * 20 + " CHARLOTTE'S CHALLENGE " + "=" * 20)
        self.solve_charlotte_challenge()
        
        # Display execution time
        elapsed = self._get_elapsed_time()
        print(f"\n" + "=" * 50)
        print(f"Total execution time: {elapsed:.2f} seconds")
        print("=" * 50)


def main() -> None:
    """Main entry point."""
    solver = OTPSolver()
    solver.run_all_challenges()


if __name__ == "__main__":
    main()