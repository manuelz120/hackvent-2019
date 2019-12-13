package at.hackvent19;

import static org.apache.commons.lang3.StringEscapeUtils.unescapeJava;

import org.apache.commons.collections4.trie.PatriciaTrie;

public class Main {
	private static final String securitytoken = "auth_token_4835989";

	@SuppressWarnings("deprecation")
	public static void main(String[] args) {
		PatriciaTrie<Integer> trie = new PatriciaTrie<Integer>();
		trie.put(securitytoken, 0);
		String input = "auth_token_483598\u0039";
		input = "auth_token_4835989\0";

		trie.put(unescapeJava(input), 0);

		System.out.println(unescapeJava(input));
		System.out.println(unescapeJava(input).equals(securitytoken));
		
		System.out.println("Contains input: " + trie.containsKey(input));
		System.out.println("Contains escaped input: " + trie.containsKey(unescapeJava(input)));
		System.out.println("Contains token: " + trie.containsKey(securitytoken));
	}

}
